from django.db import models

# Estructuración del modelo de temas para la tabla en la BD 
class temaWiki(models.Model):
    nombre_tema = models.CharField(max_length=128, null=True, blank=True)
    descripcion_tema = models.CharField(max_length=512, null=True, blank=True)

# Estructuración del modelo de artículos para la tabla en la BD
class articuloWiki(models.Model):
    titulo = models.CharField(max_length=128)
    contenido = models.CharField(max_length=1024)
    tema_relacionado = models.ForeignKey(temaWiki, null=True, blank=True, on_delete=models.SET_NULL)