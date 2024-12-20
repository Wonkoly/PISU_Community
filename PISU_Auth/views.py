from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from .forms import UserLoginForm, PerfilForm, ConfiguracionForm, CustomUserCreationForm
from django.contrib import messages
from .models import CustomUser, CentroUniversitario, Carrera

def signup_success(request):
    return render(request, 'PISU_Auth/signup_success.html')

def verify_email(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    user.is_verified = True
    user.save()
    return HttpResponse("Cuenta verificada con éxito. Ahora puedes iniciar sesión.")

# Vista de registro
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_verified = False  # Establecer como no verificado
            user.save()

            # Generar link de verificación
            verification_link = request.build_absolute_uri(f'/auth/verify/{user.id}/')

            # Enviar correo con nombre de usuario generado
            send_mail(
                'Verificación de cuenta',
                f'Hola {user.first_name}, verifica tu cuenta en el siguiente enlace: {verification_link}\n\n'
                f'Tu nombre de usuario es: {user.username}',
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )

            return redirect('signup_success')  # Redirige al mensaje de éxito
    else:
        form = CustomUserCreationForm()
    return render(request, 'PISU_Auth/signup.html', {'form': form})

# Vista de login
class CustomLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "PISU_Auth/login.html"

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)

        if user:
            if not user.is_verified:  # Verifica si la cuenta está activa
                messages.error(self.request, "Tu cuenta está inactiva. Verifica tu correo para activarla.")
                return redirect('login')
            login(self.request, user)
            return redirect(self.get_success_url())
        else:
            messages.error(self.request, "Usuario o contraseña incorrectos.")
            return redirect('login')


# Vista para Configuracion del Usuario
@login_required
def perfil_view(request):
    # Obtener el usuario actual
    user = get_object_or_404(CustomUser, id=request.user.id)

    if request.method == 'POST':
        # Si se presiona el botón para quitar la foto
        if 'remove_photo' in request.POST:
            if user.foto_perfil:  # Verifica que haya una foto de perfil
                user.foto_perfil.delete()
                user.save()
            return redirect('perfil')

        # Si se presionó el botón de guardar cambios
        form = PerfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige a la misma página después de guardar
    else:
        # Prellenar el formulario con los datos del usuario
        form = PerfilForm(instance=user)

    return render(request, 'PISU_Auth/perfil.html', {'form': form, 'user': user})


@login_required
def configuracion_view(request):
    user = request.user
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        form = ConfiguracionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({"status": "success"}, status=200)
        return JsonResponse({"status": "error", "errors": form.errors}, status=400)
    else:
        form = ConfiguracionForm(instance=user)
    
    return render(request, 'PISU_Auth/configuracion.html', {'form': form})