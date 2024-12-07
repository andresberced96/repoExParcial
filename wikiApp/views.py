from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import temaWiki,articuloWiki

def principal(request):
    temas = temaWiki.objects.all()
    return render(request,'principal.html',{
        'temas':temas
    })

def nuevo_tema(request):
    temas = temaWiki.objects.all()
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
    temas = temaWiki.objects.all()
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        contenido = request.POST.get('contenido')
        tema_relacionado = request.POST.get('tema_relacionado')
        print("id de temaWiki",tema_relacionado)
        temaObj = temaWiki.objects.get(id=tema_relacionado)
        articuloWiki.objects.create(
            titulo = titulo,
            contenido = contenido,
            tema_relacionado = temaObj
        )    
    return render(request, 'nuevo_articulo.html',{
        'temas':temas
        })
def articulos_x_tema(request,id_tema):
    temas = temaWiki.objects.all()
    tema_id = temaWiki.objects.get(id=id_tema)
    lista_articulos = tema_id.articulowiki_set.all()
    return render(request, 'articulos_x_tema.html',{
        'temas': temas,'articulos':lista_articulos, 'articulo_x_tema':tema_id.nombre_tema
    })
def articulos(request,id_articulo):
    temas = temaWiki.objects.all()
    articulo_id = articuloWiki.objects.get(id=id_articulo)
    return render(request, 'articulos.html',{
        'temas': temas, 'articulo':articulo_id
    })
def busqueda(request):
    temas = temaWiki.objects.all()
    lista_articulos = []
    if request.method == 'POST':
        buscador = request.POST.get('buscador')
        if(buscador != ""):
            lista_articulos = articuloWiki.objects.filter(titulo__icontains=buscador) 
            print("articulos",lista_articulos)
    return render(request, 'busqueda.html',{
        'temas': temas, 'articulos':lista_articulos
    })