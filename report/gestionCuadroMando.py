import os, subprocess

CUADRO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def CrearCuadroMando(nombre):
    archivo = nombre + ".pbix"
    subprocess.run(CUADRO_DIR + archivo, shell = True)

def VisualizarCuadroMando():
    pass
