from django.http import HttpResponse, HttpResponseNotFound
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
        if archivo:
            mensaje ="Cargado con exito, ya puede ver los nuevos datos en la plantilla del cuadro de mando"
        else:
            mensaje = "Archivo no valido, revise su contenido, vuelva a la opcion cargar Dataset"
        activo = ML.Optimizar(archivo)
    return render(request,"cargaCompleta.html",{'msg':mensaje})

def DescargaDataset(request):
    global activo 
    if activo == True:
        pass
    return render(request,"descarga.html",{'activo':activo})

def ProcesoDescarga(request):
    file_location = '..\\dataset\\superstore.csv'
    try:    
        with open(file_location, 'rb') as f:
           file_data = f.read()
           response = HttpResponse(file_data, content_type='text/csv')
           response['Content-Disposition'] = 'attachment; filename="superstore.csv"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    return response

def Estadisticas(request):
    global activo
    if activo == True:
        stats = ML.ObtenerEstadisticas() 
        return render(request,"estadisticas.html",{'activo':activo, 'stats':stats})
    else:
        return render(request,"estadisticas.html",{'activo':activo})


def ConsultarDashboard(request):
    Dashboard.VisualizarCuadroMando()
    return render(request,"cargaCuadro.html")

def CerrarPrograma(request):

    return HttpResponse("Cerrando el programa ...",sys.exit(0))    # Aqui hay que implementar un método para cerrar con un wait o algo parecido

