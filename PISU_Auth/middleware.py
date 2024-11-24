from django.shortcuts import redirect
from django.urls import reverse

class EnsureVerifiedMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_paths = [
            reverse('signup_success'),
            reverse('verify_email'),  # Ruta para verificar correo
            reverse('login'),         # Ruta para iniciar sesión
        ]
        if request.user.is_authenticated and not request.user.is_verified:
            if request.path not in allowed_paths:
                return redirect('signup_success')  # Redirige hasta que verifique el correo
        return self.get_response(request)
