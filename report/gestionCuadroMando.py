import subprocess

def VisualizarCuadroMando():
     return subprocess.run("plantilla.pbix" , shell = True)
