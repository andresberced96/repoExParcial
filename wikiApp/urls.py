from django.urls import path
from . import views

app_name="wikiApp"

urlpatterns = [
    path('',views.principal,name="principal"),
    path('nuevo_tema',views.nuevo_tema,name="nuevo_tema"),
    path('nuevo_articulo',views.nuevo_articulo,name="nuevo_articulo"),
]