import os, subprocess

CUADRO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def CrearCuadroMando(nombre):
    new_nombre = nombre.replace('csv' or "xlsx",'')
    archivo = new_nombre + ".pbix"
    with open(archivo, 'r'):
        pass
    subprocess.run(CUADRO_DIR + archivo, shell = True)


def VisualizarCuadroMando(archivo):
     subprocess.run(CUADRO_DIR + archivo, shell = True)
