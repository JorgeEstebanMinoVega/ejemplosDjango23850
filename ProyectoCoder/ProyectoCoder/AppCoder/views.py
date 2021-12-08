from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def inicio(request):

    return render(request, 'AppCoder/inicio.html')

def jugador(request):

    return render(request, 'AppCoder/jugador.html')

def profesor(request):

    return render(request, 'AppCoder/profesor.html')

def jugadores(request):

    return render(request, 'AppCoder/jugadores.html')





