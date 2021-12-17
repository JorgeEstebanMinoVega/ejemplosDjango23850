from django import forms


class CursoFormulario(forms.Form):

    nombre = forms.CharField(required=True)
    camada = forms.IntegerField()

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()

class CantidadEstudiantesFormulario(forms.Form):

    cantidadEstudiantes = forms.IntegerField()
    


