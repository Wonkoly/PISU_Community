# PISU_Foro/forms.py
from django import forms
from .models import Foro, Comentario

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Foro
        fields = ['titulo', 'descripcion']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
