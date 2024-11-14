# PISU_Foro/models.py
from django.db import models
from django.conf import settings  # Importar settings para usar AUTH_USER_MODEL

class Discusion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Cambiado a settings.AUTH_USER_MODEL

    def __str__(self):
        return self.titulo

class Publicacion(models.Model):
    discusion = models.ForeignKey(Discusion, on_delete=models.CASCADE, related_name='publicaciones')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Cambiado a settings.AUTH_USER_MODEL

    def __str__(self):
        return f"{self.autor.username}: {self.contenido[:30]}"

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Cambiado a settings.AUTH_USER_MODEL

    def __str__(self):
        return f"{self.autor.username}: {self.contenido[:30]}"
