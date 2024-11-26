from django.db import models
from django.conf import settings  # Usar AUTH_USER_MODEL

class Discusion(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_autor_nombre(self):
        if self.creador.anonimo:
            return "Anónimo"
        return self.creador.username

    def __str__(self):
        return self.titulo

class Publicacion(models.Model):
    discusion = models.ForeignKey(Discusion, on_delete=models.CASCADE, related_name='publicaciones')
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.autor.username}: {self.contenido[:30]}"

class Comentario(models.Model):
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios_foro')
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.publicacion.discusion.titulo}'
