from asyncio.windows_events import NULL
from django.http import HttpResponse
from django.shortcuts import render 
import report.gestionCuadroMando as Dashboard 
import src.app.OptimizationProcess as ML
import sys


def Inicio(request):

    return render(request,"inicio.html")

def CargaDataset(request):

    return render(request,"carga.html")

def CargaCompletada(request):
    if request.FILES["files"]:
        opt = ML.Optimizar(request.FILES["files"])
        if opt == NULL:
            mensaje = "Cargado con exito, ya puede acceder a todas las funciones"
        else:
            mensaje = "Archivo no valido, revise su contenido"

    return render(request,"cargaCompleta.html",{"msg":mensaje})


def DescargaDataset(request):

    return render(request,"descarga.html")

def Estadisticas(request):

    return render(request,"estadisticas.html")

def PlantillaPowerBi(request):

    return HttpResponse(Dashboard.VisualizarCuadroMando())    # Abre PowerBI para crear la plantilla del cuadro de mando que se va a usar

def CerrarPrograma(request):

    return HttpResponse("Cerrando el programa ...",sys.exit(0))    # Aqui hay que implementar un método para cerrar con un wait o algo parecido

def OptimizarDataset(request):

    return render (request,"optimizacion.html")
    