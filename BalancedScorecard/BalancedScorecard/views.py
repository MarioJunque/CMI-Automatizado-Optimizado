from django.http import HttpResponse
from django.shortcuts import render 


def Inicio(request):

    return render(request,"inicio.html")

def CargaDataset(request):

    return render(request,"carga.html")

def DescargaDataset(request):

    return render(request,"descarga.html")

def Estadisticas(request):

    return render(request,"estadisticas.html")


    