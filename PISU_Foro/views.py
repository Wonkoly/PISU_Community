# PISU_Foro/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Discusion, Publicacion, Comentario
from .forms import DiscusionForm, PublicacionForm, ComentarioForm

def lista_discusiones(request):
    discusiones = Discusion.objects.all()
    return render(request, 'PISU_Foro/lista_discusiones.html', {'discusiones': discusiones})

@login_required
def crear_discusion(request):
    if request.method == 'POST':
        form = DiscusionForm(request.POST)
        if form.is_valid():
            nueva_discusion = form.save(commit=False)
            nueva_discusion.creador = request.user
            nueva_discusion.save()
            return redirect('lista_discusiones')
    else:
        form = DiscusionForm()
    return render(request, 'PISU_Foro/crear_discusion.html', {'form': form})

def ver_discusion(request, discusion_id):
    discusion = get_object_or_404(Discusion, id=discusion_id)
    publicaciones = discusion.publicaciones.all()
    return render(request, 'PISU_Foro/ver_discusion.html', {'discusion': discusion, 'publicaciones': publicaciones})

@login_required
def crear_publicacion(request, discusion_id):
    discusion = get_object_or_404(Discusion, id=discusion_id)
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            nueva_publicacion = form.save(commit=False)
            nueva_publicacion.autor = request.user
            nueva_publicacion.discusion = discusion
            nueva_publicacion.save()
            return redirect('ver_discusion', discusion_id=discusion.id)
    else:
        form = PublicacionForm()
    return render(request, 'PISU_Foro/crear_publicacion.html', {'form': form, 'discusion': discusion})

@login_required
def crear_comentario(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, id=publicacion_id)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            nuevo_comentario = form.save(commit=False)
            nuevo_comentario.autor = request.user
            nuevo_comentario.publicacion = publicacion
            nuevo_comentario.save()
            return redirect('ver_discusion', discusion_id=publicacion.discusion.id)
    else:
        form = ComentarioForm()
    return render(request, 'PISU_Foro/crear_comentario.html', {'form': form, 'publicacion': publicacion})
