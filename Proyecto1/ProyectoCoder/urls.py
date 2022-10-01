from ProyectoCoder.views import *
from django.urls import path
urlpatterns = [
    path("", inicio, name="Inicio"),
    path("formuProfe/", formuProfe, name="formuProfes"),
    path("formuEs/", formuEstudiate, name="formuEstudiante"),
    path("formuEn/", formuEntregable, name="formuEntregable"),
    path("resultados/", buscar, name="resultado"),
    path("buscadorProfes", buscadorProfes, name="buscadorProfes"),
    ]
