from django.http import HttpResponse
from django.shortcuts import render 
import report.gestionCuadroMando as Dashboard 
import src.app.OptimizationProcess as ML
import sys

activo = False

def Inicio(request):

    return render(request,"inicio.html")

def CargaDataset(request):

    return render(request,"carga.html")

def CargaCompletada(request):
    global activo
    if request.method == "POST":
        archivo = request.FILES['document']
        print(archivo.temporary_file_path())
        contenido = request.FILES['document'].read()
        if archivo:
            mensaje ="Cargado con exito, ya puede crear la plantilla del cuadro de mando"
        else:
            mensaje = "Archivo no valido, revise su contenido, vuelva a la opcion cargar Dataset"
        activo = ML.Optimizar(contenido)
    return render(request,"cargaCompleta.html",{'msg':mensaje})

def DescargaDataset(request):
    global activo 
    if activo == True:
        pass
    return render(request,"descarga.html",{'activo':activo})

def Estadisticas(request):
    global activo
    if activo == True:
        ML.obtenerEstadisticas() 
    return render(request,"estadisticas.html",{'activo':activo})


def ConsultarDashboard(request):
    Dashboard.VisualizarCuadroMando()

    return render(request,"cargaCuadro.hmtl")  # Consulta dashboard optimizado 

def CerrarPrograma(request):

    return HttpResponse("Cerrando el programa ...",sys.exit(0))    # Aqui hay que implementar un método para cerrar con un wait o algo parecido

