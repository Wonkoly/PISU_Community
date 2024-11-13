# PISU_Foro/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Foro, Comentario
from .forms import PublicacionForm, ComentarioForm

@login_required
def lista_publicaciones(request):
    publicaciones = Foro.objects.all().order_by('-fecha_creacion')
    return render(request, 'PISU_Foro/lista_publicaciones.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Foro, id=publicacion_id)
    comentarios = publicacion.comentarios.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.foro = publicacion
            comentario.save()
            return redirect('detalle_publicacion', publicacion_id=publicacion.id)
    else:
        form = ComentarioForm()
    return render(request, 'PISU_Foro/detalle_publicacion.html', {
        'publicacion': publicacion,
        'comentarios': comentarios,
        'form': form,
    })

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.creador = request.user
            publicacion.save()
            return redirect('lista_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'PISU_Foro/crear_publicacion.html', {'form': form})
