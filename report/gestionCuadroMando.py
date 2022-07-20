import os, subprocess

CUADRO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def CrearCuadroMando(nombre):
    archivo = nombre + ".pbix"
    with open(archivo, 'r'):
        pass
    subprocess.run(CUADRO_DIR + archivo, shell = True)
    return False

def VisualizarCuadroMando(archivo):
     subprocess.run(CUADRO_DIR + archivo, shell = True)
