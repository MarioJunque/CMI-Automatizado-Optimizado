from src.app import Training
from src.app import DataWrangling
import numpy as np
import pandas as pd

data_sales = None
data_product = None
data_store = None
data = None
informe = None

def PrepararDatos(dataset):     # Convierte el dataset en un dataframe para poder manejar la informacion de forma mas sencilla
    global data_sales,data_store,data_product, data
    for file in dataset:
        if file == 'sales.csv':
            data_sales = pd.read_csv(dataset, encoding='latin1')
            data_sales = DataWrangling.Preprocesar(data_sales)
        elif file == 'store.csv':
            data_store = pd.read_csv(dataset, encoding='latin1')

    data = pd.merge(data_sales,data_store, on=['store_id'])
   

def Entrenar():
    global informe
    modelo, informe = Training.TrainModelCV(data[['SALES']].values,data['TOTAL_REVENUE'].values)
    tam = len(modelo)
    while tam:
        new_row = data[np.isin(data,['pear','apple']).any(axis=1)]
        df = df.append(new_row, ignore_index=True)
        tam-=1

    return True
    

def Optimizar(df):
    PrepararDatos(df)
    proceso = Entrenar()
    ModelConverter()
    return proceso

def ModelConverter():
     data.to_csv("..\\dataset\\superstore.csv", index=False, encoding='utf-8-sig')

        

def ObtenerEstadisticas():
    resultado = informe
    return resultado
