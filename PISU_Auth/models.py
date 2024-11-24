from django.contrib.auth.models import AbstractUser
from django.db import models

class CentroUniversitario(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    centro_universitario = models.ForeignKey(CentroUniversitario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class CustomUser(AbstractUser):
    ROLES = [
        ('administrativo', 'Administrativo'),
        ('academico', 'Académico'),
        ('alumno', 'Alumno'),
    ]
    rol = models.CharField(max_length=15, choices=ROLES)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True)
    centro_universitario = models.ForeignKey(CentroUniversitario, on_delete=models.SET_NULL, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='perfil_fotos/', null=True, blank=True)
    anonimo = models.BooleanField(default=False)
    username = models.CharField(max_length=150, unique=True, blank=True)
    is_verified = models.BooleanField(default=False)  # Nuevo campo

    def __str__(self):
        return self.username

