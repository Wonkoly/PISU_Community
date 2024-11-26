from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.text import slugify
from .models import CustomUser, Carrera

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if email.endswith('@academicos.udg.mx'):
            self.instance.rol = 'academico'
        elif email.endswith('@cuc.udg.mx'):
            self.instance.rol = 'administrativo'
        elif email.endswith('@alumnos.udg.mx'):
            self.instance.rol = 'alumno'
        else:
            raise forms.ValidationError("Correo no válido. Debe usar un dominio institucional.")
        return email
    
    def save(self, commit=True):
        user = super().save(commit=False)
        # Generar username único
        base_username = slugify(f"{user.first_name}{user.last_name[:2]}")
        username = base_username
        counter = 1
        while CustomUser.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        user.username = username

        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'})
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'})
    )


class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })

# Configuracion del Usuario
class PerfilForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'centro_universitario', 'carrera', 'foto_perfil']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'centro_universitario': forms.Select(attrs={'class': 'form-control'}),
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.centro_universitario:
            self.fields['carrera'].queryset = Carrera.objects.filter(
                centro_universitario=self.instance.centro_universitario
            )
        else:
            self.fields['carrera'].queryset = Carrera.objects.none()

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['anonimo']
        widgets = {
            'anonimo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
