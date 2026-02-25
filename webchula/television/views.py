from django.shortcuts import render
from television import models as md


# Create your views here.
def index(request):
    return render(request, "index.html")
def series(request):
    service = md.ServiceSeries()
    listaSeries = service.getSeries()
    informacion = {
        "listaseries": listaSeries
    }
    return render(request, "series.html",informacion)

def personajes(request):
    if ('idserie' in request.GET):
        service = md.ServiceSeries()
        idserie = int(request.GET["idserie"])
        personajes = service.getPersonajesSerie(idserie)
        informacion = {
            "personajes": personajes
        }
    return render(request, "personajes.html",informacion)

def insertar(request):
    service = md.ServiceSeries()
    listaSeries = service.getSeries()
    informacion = {'listaseries': listaSeries}
    if ("cajanom" in request.POST):
        nombre =  request.POST["cajanom"]
        imagen =  request.POST["cajaimg"]
        idSerie = int(request.POST["cajaids"])
        service.InsertarPersonaje(nombre,imagen,idSerie)
     
        personajes = service.getPersonajesSerie(idSerie)
        informacion = {"personajes": personajes }
        return render(request, "insertar.html",informacion)
    else:
        return render(request, "insertar.html",informacion)
        



