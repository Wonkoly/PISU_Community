from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from .models import CustomUser, Carrera, CentroUniversitario

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=255, required=True)
    carrera = forms.ModelChoiceField(queryset=Carrera.objects.all(), required=False)
    centro_universitario = forms.ModelChoiceField(queryset=CentroUniversitario.objects.all(), required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'full_name', 'email', 'carrera', 'centro_universitario', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            domain = email.split('@')[-1]
            if domain == 'academicos.udg.mx':
                self.cleaned_data['rol'] = 'academico'
            elif domain == 'cuc.udg.mx':
                self.cleaned_data['rol'] = 'administrativo'
            elif domain == 'alumnos.udg.mx':
                self.cleaned_data['rol'] = 'alumno'
            else:
                raise ValidationError("El dominio del correo no está permitido. Use un correo con dominio @academicos.udg.mx, @cuc.udg.mx o @alumnos.udg.mx.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.rol = self.cleaned_data['rol']  # Asignar el rol según el dominio
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'input-field'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'input-field'}))

# Configuracion del Usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'foto_perfil']

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['anonimo']
