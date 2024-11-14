from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Anuario
from .forms import AnuarioForm

@login_required
def anuario_view(request):
    if request.method == 'POST':
        form = AnuarioForm(request.POST, request.FILES)
        if form.is_valid():
            anuario_entry = form.save(commit=False)
            anuario_entry.usuario = request.user
            anuario_entry.save()
            return redirect('anuario')
    else:
        form = AnuarioForm()

    anuario_entries = Anuario.objects.all()
    return render(request, 'PISU_Anuario/anuario.html', {'form': form, 'anuario_entries': anuario_entries})
