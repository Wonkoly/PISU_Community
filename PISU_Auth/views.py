from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import UserSignupForm, UserLoginForm

# Vista de registro
def signup_view(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserSignupForm()
    return render(request, 'PISU_Auth/signup.html', {'form': form})

# Vista de login
class CustomLoginView(LoginView):
    template_name = 'PISU_Auth/login.html'
    authentication_form = UserLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('lista_publicaciones')  # Cambia 'home' por la URL de tu página principal
