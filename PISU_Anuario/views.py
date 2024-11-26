from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Foto, Comentario, CompartirFoto
from PISU_Auth.models import CustomUser  # Ajusta la ruta si es necesario
from .forms import FotoForm, ComentarioForm  # Crea estos formularios
from django.contrib import messages

@login_required
def anuario(request):
    # Lista todas las fotos
    fotos = Foto.objects.all().order_by('-fecha_publicacion')
    return render(request, 'PISU_Anuario/Anuario.html', {'fotos': fotos})

@login_required
def agregar_foto(request):
    # Formulario para agregar una foto
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.autor = request.user
            foto.save()
            messages.success(request, 'Foto agregada exitosamente.')
            return redirect('anuario')
    else:
        form = FotoForm()
    return render(request, 'PISU_Anuario/agregar_foto.html', {'form': form})

@login_required
def ver_foto(request, foto_id):
    # Ver una foto individual
    foto = get_object_or_404(Foto, id=foto_id)
    comentarios = Comentario.objects.filter(foto=foto).order_by('-fecha_comentario')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.autor = request.user
            comentario.foto = foto
            comentario.save()
            messages.success(request, 'Comentario agregado.')
            return redirect('ver_foto', foto_id=foto.id)
    else:
        form = ComentarioForm()
    return render(request, 'PISU_Anuario/ver_foto.html', {'foto': foto, 'comentarios': comentarios, 'form': form})

@login_required
def editar_foto(request, foto_id):
    # Editar una foto (solo el autor)
    foto = get_object_or_404(Foto, id=foto_id, autor=request.user)
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES, instance=foto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Foto editada exitosamente.')
            return redirect('anuario')
    else:
        form = FotoForm(instance=foto)
    return render(request, 'PISU_Anuario/editar_foto.html', {'form': form})

@login_required
def eliminar_foto(request, foto_id):
    # Eliminar una foto (solo el autor)
    foto = get_object_or_404(Foto, id=foto_id, autor=request.user)
    if request.method == 'POST':
        foto.delete()
        messages.success(request, 'Foto eliminada exitosamente.')
        return redirect('anuario')
    return render(request, 'PISU_Anuario/eliminar_foto.html', {'foto': foto})

@login_required
def compartir_foto(request, foto_id):
    # Compartir una foto con otro usuario
    foto = get_object_or_404(Foto, id=foto_id)
    if request.method == 'POST':
        receptor_id = request.POST.get('receptor_id')
        receptor = get_object_or_404(CustomUser, id=receptor_id)
        if receptor != request.user:
            CompartirFoto.objects.create(foto=foto, receptor=receptor)
            messages.success(request, f'Foto compartida con {receptor.username}.')
        else:
            messages.error(request, 'No puedes compartir la foto contigo mismo.')
        return redirect('ver_foto', foto_id=foto.id)
    usuarios = CustomUser.objects.exclude(id=request.user.id)
    return render(request, 'PISU_Anuario/compartir_foto.html', {'foto': foto, 'usuarios': usuarios})
