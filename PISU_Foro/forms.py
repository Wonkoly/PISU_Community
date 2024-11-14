# PISU_Foro/forms.py
from django import forms
from .models import Discusion, Publicacion, Comentario

class DiscusionForm(forms.ModelForm):
    class Meta:
        model = Discusion
        fields = ['titulo', 'descripcion']

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['contenido']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido']
