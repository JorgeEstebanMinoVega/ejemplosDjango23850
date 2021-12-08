from django.urls import path
from django.urls.conf import include
from AppCoder import views

urlpatterns = [
    
    path('inicio', views.inicio),
    path('jugador', views.jugador),
    path('profesor', views.profesor),
    path('jugadores', views.jugadores),




    

    
]