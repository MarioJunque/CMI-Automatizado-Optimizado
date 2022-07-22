import subprocess

CUADRO_DIR = "cd..\\..\\report\\plantilla.pbix"

def VisualizarCuadroMando():
     subprocess.run(CUADRO_DIR , shell = True)
