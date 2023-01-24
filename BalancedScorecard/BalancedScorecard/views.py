from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render 
import report.gestionCuadroMando as Dashboard 
import src.app.OptimizationProcess as ML
import sys




activo = False

def Inicio(request):    # Carga la pantalla de inicio

    return render(request,"inicio.html")

def CargaDataset(request):

    return render(request,"carga.html")

def CargaCompletada(request):    # Carga en el sistema el conjunto de datos para procesarlo
    global activo
    if request.method == "POST":

        archivo = request.FILES['document']
        producto = request.POST.get('product', '')

        print('Se ha cargado el archivo',archivo, 'y el producto',producto)
        if archivo:
            mensaje ="Cargado con exito, ya puede ver los nuevos datos en la plantilla del cuadro de mando"
        else:
            mensaje = "Archivo no valido, revise su contenido, vuelva a la opcion cargar Dataset"
        activo = ML.Optimizar(archivo,producto)
    return render(request,"cargaCompleta.html",{'msg':mensaje})

def DescargaDataset(request):  # Pantalla de descarga de archivo
    global activo 
    if activo == True:
        pass
    return render(request,"descarga.html",{'activo':activo})

def ProcesoDescarga(request):   # Inicia el proceso de descarga del archivo optimizado con los nuevos registros de prediccion
    file_location = '..\\dataset\\sales.csv'
    try:    
        with open(file_location, 'rb') as f:
           file_data = f.read()
           response = HttpResponse(file_data, content_type='text/csv')
           response['Content-Disposition'] = 'attachment; filename="sales.csv"'

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')
    return response

def Estadisticas(request):     # Carga la pantalla de estadísticas
    global activo
    if activo == True:
        stats = ML.ObtenerEstadisticas() 
        return render(request,"estadisticas.html",{'activo':activo, 'stats':stats})
    else:
        return render(request,"estadisticas.html",{'activo':activo})


def ConsultarDashboard(request):      # Abre Power BI para ver el CMI
    Dashboard.VisualizarCuadroMando()
    return render(request,"cargaCuadro.html")

def CerrarPrograma(request): # Cierra el programa
    sys.exit(0)


