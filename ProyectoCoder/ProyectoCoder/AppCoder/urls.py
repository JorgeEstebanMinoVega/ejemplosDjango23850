from django.urls import path
from django.urls.conf import include
from AppCoder import views

urlpatterns = [
    
    path('inicio', views.inicio, name="Inicio"),
    path('curso', views.curso, name="Curso"),
    path('profesor', views.profesor, name="Profesor"),
    path('estudiante', views.estudiante, name="Estudiante"),
    path('cantidadEstudiantes', views.cantidadEstudiantes, name="CantidadEstudiantes"),
    path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    path('estudianteFormulario', views.estudianteFormulario, name="estudianteFormulario"),
    path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    path('cantidadEstuFormulario', views.cantidadEstuFormulario, name="CantidadEstuFormulario"),
    



    

    
]