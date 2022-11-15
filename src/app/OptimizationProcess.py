from src.app import Training
from src.app import DataWrangling
from zipfile import ZipFile
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np
import random 

data_sales = None
data_store = None
data = None
df_tam_pred = None
informe = None


# Comienza el proceso de optimización

def Optimizar(df):
    PrepararDatos(df)
    proceso = Entrenar()
    ModelConverter()
    return proceso

# Convierte el dataset en un dataframe para poder manejar la informacion de forma mas sencilla y limpia los datos 

def PrepararDatos(dataset):     
    global data_sales,data_store, data, df_tam_pred
    for file in dataset:
        if str(file) == 'sales.csv':
            diclist = {"product_id": object,"store_id": object,"date": object, "sales":float, "revenue": float, "stock":float, "price":float,"promo_type_1":object, "promo_bin_1":object,"promo_type_2":object, "promo_bin_2":object, "promo_discount_2":object, "promo_discount_type_2": object }                                        
            data_sales = pd.read_csv(file, dtype= diclist)      
            df_sales = data_sales.drop(columns=['promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2'])
            df_sales_final = DataWrangling.Preprocesar(df_sales)
        elif str(file) == 'store_cities.csv':
            data_store = pd.read_csv(file)
    
    data = pd.merge(df_sales_final,data_store, on=['store_id'])     # une tabla sales y store por id de tienda

    df_tam_pred = len(data)    # Guarda el tamaño del dataframe para saber cuantas muestras nuevas generará luego

# Entrena el modelos con los datos preparados   

def Entrenar():
    global informe, data_sales,data, df_tam_pred
    best_products = data.groupby("product_id")
    best_products = best_products[best_products["product_id"].value_counts() >= 50]
    sample_products = best_products.sample(n = df_tam_pred, replace=True )

    # Aqui se obtienen los datos de la predicción y las métricas del algoritmo escogido
    modelo, informe = Training.TrainModelCV(best_products[['sales','stock']].values,data['revenue'].values)

    # Copia de las predicciones en nuevos registros
    tam = len(modelo)
    while tam:
        new_row = sample_products[tam,:]       # usar metodo sample() de pandas para sacar una fila aleatoria y modificarla con nueva fecha y producto
        fechaNueva = pd.to_datetime('2020-06-30')
        new_row.at [0,'date'] = fechaNueva
        new_row.at[0,'revenue'] =  modelo[tam]

        data_sales = data_sales.append(new_row, ignore_index=True)
        tam-=1

    return True

# Convierte de vuelta a formato csv los archivos usados y se comprimen para reducir el tamaño de archivo

def ModelConverter():
    global data_sales,data_store
    data_sales.to_csv("..\\dataset\\sales.csv", index=False)     # , encoding='utf-8-sig'

    # Comprime los archivos para que ocupen menos

    with ZipFile('sales.zip', 'w') as myzip:
        myzip.write('sales.csv')

# Prepara los datos para el informe de estadísticas en la aplicación 

def ObtenerEstadisticas():
    resultado = informe
    return resultado
