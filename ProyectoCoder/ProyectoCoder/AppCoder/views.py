from django import forms
from django.forms.formsets import MIN_NUM_FORM_COUNT
from django.shortcuts import render

from django.http import HttpResponse

from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario
from AppCoder.forms import EstudianteFormulario
from AppCoder.models import Estudiante
from AppCoder.forms import ProfesorFormulario
from AppCoder.models import Profesor
from AppCoder.models import CantidadEstudiantes
from AppCoder.forms import CantidadEstudiantesFormulario

def cursoFormulario(request):

    if request.method == "POST":

        formularioCurso = CursoFormulario(request.POST)

        if formularioCurso.is_valid():

            informacion = formularioCurso.cleaned_data

            cursoInsta = Curso(nombre = request.POST["nombre"], camada = request.POST["camada"])

            cursoInsta.save()
        
        return render(request, 'AppCoder/inicio.html')

    else:

        formularioCurso = CursoFormulario()
        
    return render(request, 'AppCoder/cursoFormulario.html', {"miFormulario":formularioCurso})

def estudianteFormulario(request):

    if request.method == "POST":

        formularioEstudiante = EstudianteFormulario(request.POST)

        if formularioEstudiante.is_valid():

            informacion = formularioEstudiante.cleaned_data

            estudianteInsta = Estudiante(nombre = request.POST["nombre"], apellido = request.POST["apellido"], edad = request.POST["edad"])

            estudianteInsta.save()
        
        return render(request, 'AppCoder/inicio.html')

    else:

        formularioEstudiante = EstudianteFormulario()
        
    return render(request, 'AppCoder/estudianteFormulario.html', {"miFormulario":formularioEstudiante})

def profesorFormulario(request):

    if request.method == "POST":

        formularioProfesor = ProfesorFormulario(request.POST)

        if formularioProfesor.is_valid():

            informacion = formularioProfesor.cleaned_data

            profesorInsta = Profesor(nombre = request.POST["nombre"], apellido = request.POST["apellido"], edad = request.POST["edad"])

            profesorInsta.save()
        
        return render(request, 'AppCoder/inicio.html')

    else:

        formularioProfesor = ProfesorFormulario()
        
    return render(request, 'AppCoder/profesorFormulario.html', {"miFormulario":formularioProfesor})

def cantidadEstuFormulario(request):

    if request.method == "POST":

        formularioCantidadEstu = CantidadEstudiantesFormulario(request.POST)

        if formularioCantidadEstu.is_valid():

            informacion = formularioCantidadEstu.cleaned_data

            cantidadEstuInsta = CantidadEstudiantes(cantidadEstudiantes = request.POST["cantidadEstudiantes"])

            cantidadEstuInsta.save()
        
        return render(request, 'AppCoder/inicio.html')

    else:

        formularioCantidadEstu = CantidadEstudiantesFormulario()
        
    return render(request, 'AppCoder/cantidadEstuFormulario.html', {"miFormulario":formularioCantidadEstu})



def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def curso(request):

    return render(request, 'AppCoder/curso.html')

def profesor(request):

    return render(request, 'AppCoder/profesor.html')

def estudiante(request):

    return render(request, 'AppCoder/estudiante.html')

def cantidadEstudiantes(request):

    return render(request, 'AppCoder/cantidadestudiantes.html')






