from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Formulario de Registro
class UserSignupForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        widgets = {
            'password': forms.PasswordInput()
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email.endswith('@alumnos.udg.mx'):
            raise ValidationError("El correo debe ser del dominio '@alumnos.udg.mx'")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está registrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# Formulario de Login
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Nombre de usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
