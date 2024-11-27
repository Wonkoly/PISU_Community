from django.contrib import admin
from .models import Foto, Comentario, CompartirFoto

@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'autor__username', 'descripcion')
    list_filter = ('fecha_publicacion',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('foto', 'contenido', 'fecha_comentario', 'autor')
    search_fields = ('contenido', 'autor__username', 'foto__titulo')
    list_filter = ('fecha_comentario',)

@admin.register(CompartirFoto)
class CompartirFotoAdmin(admin.ModelAdmin):
    list_display = ('foto', 'receptor', 'fecha_compartida')
    search_fields = ('foto__titulo', 'receptor__username')
    list_filter = ('fecha_compartida',)