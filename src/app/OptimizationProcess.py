
import pandas as pd
import DataWrangling, Training, Evaluate

def convertirDataframe(dataset, format):
    if format == 'csv':
        archivo = pd.read_csv(dataset, encoding='Latin-1')
    elif format == 'xlsx':
        archivo = pd.read_excel(dataset, sheet_name=None)
    return archivo

def PrepararDatos(dataset,format):
    df = convertirDataframe(dataset,format)
    datos = DataWrangling.Limpieza(df)
    return datos


def Entrenar(datos):
    modelo = Training.TrainModelCV(datos)
    return modelo


def Evaluar(modelo):
     mse,rmse,r2 = Evaluate.evaluacion(modelo)
     return mse,rmse,r2
     

def Optimizar(df):
    # datos = PrepararDatos(df)
    modelo = Entrenar(df)
    return modelo


def ModelConverter(modelo):
    if format == 'csv':
        archivo = modelo.to_csv('optimizacion.csv')
    elif format == 'xlsx':
        archivo = modelo.to_excel('optimizacion.xslx')
    return archivo
