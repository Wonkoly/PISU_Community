from django import forms
from .models import Anuario

class AnuarioForm(forms.ModelForm):
    class Meta:
        model = Anuario
        fields = ['foto', 'descripcion']
