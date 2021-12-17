from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):

        return f"CURSO:\n{self.nombre} CAMADA:\n{self.camada}"

class Estudiante(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):

        return f"NOMBRE:\n{self.nombre} APELLIDO:\n{self.apellido} EDAD:\n{self.edad}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()

    def __str__(self):

        return f"NOMBRE:\n{self.nombre} APELLIDO:\n{self.apellido} EDAD:\n{self.edad}"

class CantidadEstudiantes(models.Model):

    cantidadEstudiantes = models.IntegerField()

    def __str__(self):

        return f"CANTIDADESTUDIANTES:\n {self.cantidadEstudiantes}"

    