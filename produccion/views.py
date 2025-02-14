from django.shortcuts import render, get_object_or_404, redirect
from .models import Produccion
from .forms import ProduccionForms

def listado_producciones(request):
    producciones = Produccion.objects.select_related('color', 'talla', 'estado', 'categoria').all()
    return render(request, 'produccion.html', {'producciones': producciones})

def gestion_produccion(request, pk=None):
    produccion = get_object_or_404(Produccion, pk=pk) if pk else None

    if request.method == 'POST':
        form = ProduccionForms(request.POST, instance=produccion)
        if form.is_valid():
            form.save()
            return redirect('lista_producciones')
    else:
        form = ProduccionForms(instance=produccion)

    return render(request, 'produccion.html', {
        'producciones': Produccion.objects.select_related('color', 'talla', 'estado', 'categoria').all(),
        'form': form,
        'produccion': produccion,
    })