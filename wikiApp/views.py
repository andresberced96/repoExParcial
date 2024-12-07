from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import temaWiki,articuloWiki

temas = temaWiki.objects.all()

def principal(request):
    return render(request,'principal.html',{
        'temas':temas
    })

def nuevo_tema(request):
    if request.method == 'POST':
        nombre_tema = request.POST.get('nombre_tema')
        descripcion_tema = request.POST.get('descripcion_tema')
        temaWiki.objects.create(
            nombre_tema=nombre_tema,
            descripcion_tema=descripcion_tema
        )
    return render(request, 'nuevo_tema.html',{
        'temas':temas
        })

def nuevo_articulo(request):
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        tema_relacionado = request.POST.get('tema_relacionado')
        temaObj = temaWiki.objects.get(id=tema_relacionado)
        temaWiki.objects.create(
            titulo = titulo,
            contenido = contenido,
            tema_relacionado = temaObj
        )    
    return render(request, 'nuevo_articulo.html',{
        'temas':temas
        })