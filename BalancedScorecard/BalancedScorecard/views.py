from django.http import HttpResponse
from django.shortcuts import render 
from src.app.PowerBiEvents import llamadaBI
import sys


def Inicio(request):

    return render(request,"inicio.html")

def CargaDataset(request):

    return render(request,"carga.html")

def DescargaDataset(request):

    return render(request,"descarga.html")

def Estadisticas(request):

    return render(request,"estadisticas.html")

def PlantillaPowerBi(request):

    return HttpResponse(llamadaBI())    # Abre PowerBI para crear la plantilla del cuadro de mando que se va a usar

def CerrarPrograma(request):

    return HttpResponse("Cerrando el programa ...",sys.exit(0))    # Aqui hay que implementar un método para cerrar con un wait o algo parecido

def OptimizarDataset(request):

    return render (request,"optimizacion.html")
    