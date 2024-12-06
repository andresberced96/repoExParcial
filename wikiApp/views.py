
from django.shortcuts import render
from django.http import HttpResponse

def principal(request):
    return render(request, 'principal.html')

def nuevo_tema(request):
    return render(request, 'nuevo_tema.html')

def nuevo_articulo(request):
    return render(request, 'nuevo_articulo.html')