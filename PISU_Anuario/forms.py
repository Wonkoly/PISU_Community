from django import forms
from .models import Foto, Comentario

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['titulo', 'imagen', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
