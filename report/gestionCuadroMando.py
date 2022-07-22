import subprocess

CUADRO_DIR = "cd..\\..\\report\\plantilla.pbix"

def CrearCuadroMando():
    cadena = "C:\\Users\\mario\\AppData\\Local\\Microsoft\\WindowsApps\\Microsoft.MicrosoftPowerBIDesktop_8wekyb3d8bbwe\\PBIDesktopStore.exe"
    #path = cadena.replace( "\",'\\')
    subprocess.run(cadena , shell = True)
    return True

def VisualizarCuadroMando():
     subprocess.run(CUADRO_DIR , shell = True)
