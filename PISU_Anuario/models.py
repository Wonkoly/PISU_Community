# Create your models here.
from django.db import models
from django.conf import settings

class Anuario(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='anuario_fotos/')
    descripcion = models.TextField(max_length=255)
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.descripcion[:20]}"
