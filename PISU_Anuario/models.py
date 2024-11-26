from django.db import models
from django.conf import settings  

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='anuario_fotos/')
    descripcion = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fotos_anuario')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comentarios_anuario')
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comentario de {self.autor} en {self.foto.titulo}'

class CompartirFoto(models.Model):
    foto = models.ForeignKey(Foto, on_delete=models.CASCADE, related_name='compartidas')
    receptor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='fotos_compartidas')
    fecha_compartida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.foto.titulo} compartida con {self.receptor}'
