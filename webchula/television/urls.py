from django.urls import path
from television import views

urlpatterns =[
    path("", views.index, name="index"),
    path("series/", views.series, name="series"),
    path("personajes/",views.personajes, name ="personajes"),
    path("insertar/", views.insertar, name="insertar"),
]