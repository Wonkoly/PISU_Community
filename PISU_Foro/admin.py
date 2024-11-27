from django.contrib import admin
from .models import Discusion, Publicacion, Comentario

@admin.register(Discusion)
class DiscusionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_creacion', 'creador')
    search_fields = ('titulo', 'creador__username')
    list_filter = ('fecha_creacion',)

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('discusion', 'contenido', 'fecha_creacion', 'autor')
    search_fields = ('contenido', 'autor__username', 'discusion__titulo')
    list_filter = ('fecha_creacion',)

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'contenido', 'fecha_comentario', 'autor')
    search_fields = ('contenido', 'autor__username', 'publicacion__contenido')
    list_filter = ('fecha_comentario',)
