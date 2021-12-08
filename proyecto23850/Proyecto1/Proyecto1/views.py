from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context
from django.template import loader

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

    mejorEstudiante = "Ilan fritzler"

    nota = 8.9

    fecha = datetime.now()

    estudiantesMasSimpaticos = ["Juanse","Nadia","Cristo","Laura"]

    dicc = {"nombre":mejorEstudiante, "nota": nota, "fecha": fecha, "estudiantes": estudiantesMasSimpaticos}

    plantilla = loader.get_template("template1.html")


    #miHTML = open("C:/Users/Familia/Desktop/proyecto23850/Proyecto1/Proyecto1/plantillas/template1.html")

    #plantilla = Template(miHTML.read()) 

    #miHTML.close()

    #miContexto = Context(dicc)

    #documento = plantilla.render(miContexto)

    documento = plantilla.render(dicc)

    return HttpResponse(documento)