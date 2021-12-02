from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludo(request):
    
    return HttpResponse("Soy Esteban - Hola Django - Coder")

def segundaVista(request):
    
    return HttpResponse("----YA SOMOS PROGRAMADORES WEB----")

def dia(request):

    variable = datetime.now()

    return HttpResponse(f"Hoy es un gran dia:<br>{variable}")

def apellido(request, apellido):

    fecha = datetime.now()
    return HttpResponse(f"El alumno de coder {apellido} es muy bueno..<br> por lo menos hoy {fecha}")

def probandoTemplate(request):

    miHTML = open("C:/Users/Familia/Desktop/proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")

    plantilla = Template(miHTML.read()) 

    miHTML.close()

    miContexto = Context()

    documento = plantilla.render(miContexto)

    return HttpResponse(documento)