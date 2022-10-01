from calendar import c
from re import template
from ast import MatchMapping
from unicodedata import name
from django.http import HttpResponse
from django.template import Template,  Context
from ProyectoCoder.models import MiFamily, entregable, profesor, estudiantes1
from django.shortcuts import render
from ProyectoCoder.forms import *

def probandoTemplate(self):

	miHtml = open("C:/Users/tomas/Desktop/Python/Proyecto1/Proyecto1/Plantillas/template1.html")

	plantilla = Template(miHtml.read())

	miHtml.close()

	miContexto = Context()

	documento = plantilla.render(miContexto)

	return HttpResponse(documento)

def Family(request):

	mama = MiFamily(nombre = "Carina", edad = 47, fecha_nac="1975-05-16")
	mama.save()
	papa = MiFamily(nombre = "Edgar", edad = 52, fecha_nac="1970-01-26")
	papa.save()
	hermano = MiFamily(nombre = "Ignacio", edad = 10, fecha_nac="2011-11-07" )
	hermano.save()
	return render(request, "ProyectoCoder/Family.html",{"mama":mama,"papa":papa,"hermano":hermano})


def formuProfe(request):
	if request.method=="POST":
		formulario1 = FormularioProfesor(request.POST)
		if formulario1.is_valid(): #manera de ver si tenemos errores
			
			info = formulario1.cleaned_data
			
			ProfesorF = profesor(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"], profesion=info["profesion"])

			ProfesorF.save() #se realiza el gaurdado en la base de datos

			return render(request, "ProyectoCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacio o la podemos redireccionar a otra parte de la pagina
	
	else:
		formulario1 = FormularioProfesor() # mustra el formulario vacio
	
	return render(request, "ProyectoCoder/formuP.html", {"form1":formulario1})

def formuEstudiate(request):
	if request.method=="POST":
		formulario2 = FormularioEstudiante(request.POST)
		if formulario2.is_valid(): #manera de ver si tenemos errores
			
			info = formulario2.cleaned_data
			
			estudianteF = estudiantes1(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

			estudianteF.save() #se realiza el gaurdado en la base de datos

			return render(request, "ProyectoCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacio o la podemos redireccionar a otra parte de la pagina
	
	else:
		formulario2 = FormularioEstudiante() # mustra el formulario vacio
	
	return render(request, "ProyectoCoder/formuEs.html", {"form2":formulario2})

def formuEntregable(request):
	if request.method=="POST":
		formulario3 = FormularioEntregable(request.POST)
		if formulario3.is_valid(): #manera de ver si tenemos errores
			
			info = formulario3.cleaned_data
			
			entregableF = entregable(nombre=info["nombre"], fechaDeEntrega=info["fechaDeEntrega"])

			entregableF.save() #se realiza el gaurdado en la base de datos

			return render(request, "ProyectoCoder/inicio.html") #nos vuelve a mostrar la pagina del formulario vacio o la podemos redireccionar a otra parte de la pagina
	
	else:
		formulario3 = FormularioEntregable() # mustra el formulario vacio
	
	return render(request, "ProyectoCoder/formuEn.html", {"form3":formulario3})

def buscadorProfes(request):
	
	return render(request, "ProyectoCoder/buscadorProfe.html")

def buscar(request):
	if request.GET["nombre"]:
		nombre = request.GET["nombre"]
		profe = profesor.objects.filter(nombre__icontains=nombre)

		return render(request, "ProyectoCoder/resultados.html", {"profes":profe, "nombre":nombre})
	else:
		mensaje = "No enviste los datos"
	return HttpResponse(mensaje)

def inicio(request): 

	return render(request, "ProyectoCoder/inicio.html")