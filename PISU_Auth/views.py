from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, UserLoginForm, PerfilForm, ConfiguracionForm

# Vista de registro
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.full_name = form.cleaned_data.get('full_name')  # Obtener full_name del formulario
            user.save()
            return redirect('login')
        else:
            return render(request, 'PISU_Auth/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
    return render(request, 'PISU_Auth/signup.html', {'form': form})

# Vista de login
class CustomLoginView(LoginView):
    template_name = 'PISU_Auth/login.html'
    authentication_form = UserLoginForm  # Usar el formulario personalizado
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lista_discusiones')  # Cambia 'lista_discusiones' por la URL de tu página principal

# Vista para Configuracion del Usuario
@login_required
def perfil_view(request):
    user = request.user
    if request.method == 'POST':
        form = PerfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = PerfilForm(instance=user)
    return render(request, 'PISU_Auth/perfil.html', {'form': form})

@login_required
def configuracion_view(request):
    user = request.user
    if request.method == 'POST':
        form = ConfiguracionForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('configuracion')
    else:
        form = ConfiguracionForm(instance=user)
    return render(request, 'PISU_Auth/configuracion.html', {'form': form})
