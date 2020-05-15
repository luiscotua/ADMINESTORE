from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from checklist.models import Checkpieza
from piezas.models import Pieza, Categoria


# Create your views here.
def inicio(request):
    return render(request, 'core/inicio.html')


@login_required(redirect_field_name='core/visita.html')
def visita_visitar(request, id_checkpieza):
    r = get_object_or_404(Checkpieza, id_checkpieza=id_checkpieza)
    c = list(Categoria.objects.all())
    p = Pieza.objects.all().order_by('categoria')
    
    context = admin.site.each_context(request)
    context.update({
        'title': 'Gestión de Visitas',
        'r': r,
        'c': c,
        'p': p,
    })
    return render(request, 'core/visita.html', context)
