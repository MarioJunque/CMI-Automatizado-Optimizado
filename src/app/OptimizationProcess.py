
# Carga de librerias

from src.app import Training
from src.app import DataWrangling
from zipfile import ZipFile
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import random 

# Definición de variables globales

data_sales = None
df_sales = None
data_store = None
data = None
df_tam_pred = None
informe = None


# Ejecucion el proceso de optimización

def Optimizar(df):
    PrepararDatos(df)
    proceso = Entrenar()
    ModelConverter()
    return proceso

# Convierte el dataset en un dataframe para poder manejar la informacion de forma mas sencilla y limpia los datos 

def PrepararDatos(dataset):     
    global data_sales,data_store, data, df_tam_pred, df_sales 
    for file in dataset:
        if str(file) == 'sales.csv':
            diclist = {"product_id": object,"store_id": object,"date": object, "sales":float, "revenue": float, "stock":float, "price":float,"promo_type_1":object, "promo_bin_1":object,"promo_type_2":object, "promo_bin_2":object, "promo_discount_2":object, "promo_discount_type_2": object }                                        
            data_sales = pd.read_csv(file, dtype= diclist, sep= ",")      
            df_sales = DataWrangling.Preprocesar(data_sales.iloc[0:30000])
            print(df_sales.head())
            df_sales_final = df_sales.drop(columns=['promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2'])
        elif str(file) == 'store_cities.csv':
            data_store = pd.read_csv(file)
    
    data = pd.merge(df_sales_final,data_store, on=['store_id'])     # une tabla sales y store por id de tienda

    df_tam_pred = len(data)    # Guarda el tamaño del dataframe para saber cuantas muestras nuevas generará luego

# Entrena el modelos con los datos preparados   

def Entrenar():
    global informe, data_sales,data, df_tam_pred, df_sales
    # best_products = data['product_id'].value_counts()[:10]
    sample_products = df_sales.sample(n = 30000, replace=True )   # n = df_tam_pred

    # Aqui se obtienen los datos de la predicción y las métricas del algoritmo escogido
    modelo, informe = Training.TrainModelCV(data[['sales','price']].values,data['revenue'].values)

    # Copia de las predicciones en nuevos registros
    
    tam = 2
    # tam = len(modelo)
    while tam:
        print('modelo:',tam,'sample:',len(sample_products))
        index = tam - 1 
        new_row = sample_products.iloc[index]      
        fechaNueva = pd.to_datetime('03/06/20')
        new_row.at ['date'] = fechaNueva
        new_row.at['revenue'] =  modelo[tam]
        print(new_row)

        df_sales =pd.concat([df_sales,new_row.to_frame().T], ignore_index=True)
        tam-=1
    
    print(df_sales.tail())
    


    return True

# Convierte de vuelta a formato csv los archivos usados y se comprimen para reducir el tamaño de archivo

def ModelConverter():
    global df_sales
    df_sales.to_csv("..\\dataset\\sales.csv", index=False)     # , encoding='utf-8-sig'

    # Comprime los archivos para que ocupen menos

    #with ZipFile('sales.zip', 'w') as myzip:
    #    myzip.write('..\dataset\sales.csv"')

# Prepara los datos para el informe de estadísticas en la aplicación 

def ObtenerEstadisticas():
    resultado = informe
    return resultado
