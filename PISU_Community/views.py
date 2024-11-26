from django.shortcuts import render
from PISU_Anuario.models import Foto
from PISU_Foro.models import Discusion

def index(request):
    return render(request, 'index.html')

def buscar(request):
    query = request.GET.get('q', '')  # Obtén el término de búsqueda

    # Resultados del anuario
    fotos = Foto.objects.filter(titulo__icontains=query) if query else []

    # Resultados del foro
    discusiones = Discusion.objects.filter(titulo__icontains=query) if query else []

    # Renderiza los resultados
    return render(request, 'buscar.html', {
        'query': query,
        'fotos': fotos,
        'discusiones': discusiones,
    })
