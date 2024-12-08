from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import temaWiki,articuloWiki

#Redirección a la vista principal listando los temas (se envían a la vista como una lista)
def principal(request):
    temas = temaWiki.objects.all()
    return render(request,'principal.html',{
        'temas':temas
    })

#Creación de nuevo tema, se listan todos los temas, se consistencia que el tema a crear no exista en la BD
#Se hace el envío de los parámetros nombre_tema y descripcion_tema cuando se pulsa el botón del formulario
#Finalmente se muestra la misma vista
def nuevo_tema(request):
    temas = temaWiki.objects.all()
    tema_repetido = []
    if request.method == 'POST':
        nombre_tema = request.POST.get('nombre_tema')
        descripcion_tema = request.POST.get('descripcion_tema')
        try:
            tema_repetido = temaWiki.objects.filter(nombre_tema__iexact=nombre_tema)
            print("Entro en fase buena",tema_repetido[0].nombre_tema)
        except:
            temaWiki.objects.create(
                nombre_tema=nombre_tema,
                descripcion_tema=descripcion_tema
            )
    return render(request, 'nuevo_tema.html',{
        'temas':temas
        })

#Similar al caso anterior, pero no se consistencia la existencia de un artículo
#Se relaciona la creación del artículo a los temas preexistentes
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

#Se realiza la obtención de los artículos por tema mediante el id del tema pasado como
#parámetro en la definición de layout.html, se hace el envío de la lista de articulos y del nombre del tema
def articulos_x_tema(request,id_tema):
    temas = temaWiki.objects.all()
    tema_id = temaWiki.objects.get(id=id_tema)
    lista_articulos = tema_id.articulowiki_set.all()
    return render(request, 'articulos_x_tema.html',{
        'temas': temas,'articulos':lista_articulos, 'articulo_x_tema':tema_id.nombre_tema
    })

#Se obtienen los datos del artículo mediante el id enviado en los enlaces de articulos_x_tema.html
def articulos(request,id_articulo):
    temas = temaWiki.objects.all()
    articulo_id = articuloWiki.objects.get(id=id_articulo)
    return render(request, 'articulos.html',{
        'temas': temas, 'articulo':articulo_id
    })

#Similar a articulos_x_tema, pero aquí se agrupan los artículos por el título buscado, se realiza
#una validación de que el título del artículo contenga la palabra buscada sin importar las mayúsculas
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