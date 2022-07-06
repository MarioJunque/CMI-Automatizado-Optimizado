import numpy as np
import pandas as pd
import DataWrangling, Training, Evaluate


def PrepararDatos(df):
    datos = DataWrangling.Limpieza(df)
    return datos


def Entrenar(datos):
    modelo = Training.TrainModelCV(datos)
    return modelo


def Evaluar(modelo):
     prediccion, mediaCV, m , n, recall, precision = Evaluate.evaluacion(modelo)
     return prediccion, mediaCV, m, n, recall, precision
     

def Optimizar(df):
    datos = PrepararDatos(df)
    modelo = Entrenar(datos)


def ModelConverter(modelo):
    archivo = modelo.to_csv('optimizacion.csv')
    return archivo
