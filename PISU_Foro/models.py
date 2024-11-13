from django.db import models
from django.contrib.auth.models import User

class Foro(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="foros_creados")

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    foro = models.ForeignKey(Foro, on_delete=models.CASCADE, related_name="comentarios")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="comentarios_foro")
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.usuario} en {self.foro}'
