from src.app import Training
import numpy as np
import pandas as pd

data = None



archivoOptimizado = None

def PrepararDatos(dataset):
    global data
    data = pd.read_csv(dataset, encoding='latin1')
   
 
   

def Entrenar():
    modelo = Training.TrainModelCV(data[['Quantity','Sales','Discount']].values,data['Profit'].values)
    data[['prediccion']] = pd.DataFrame(modelo)
    print ( data[['prediccion']])
    #data['prediccion'] = tabla_Orders["prediccion"].fillna(0)
    return True
    

def Optimizar(df):
    PrepararDatos(df)
    proceso = Entrenar()
    ModelConverter()
    return proceso

def ModelConverter():
     data.to_csv("..\\dataset\\superstore.csv")

        

def obtenerEstadisticas():
    pass
