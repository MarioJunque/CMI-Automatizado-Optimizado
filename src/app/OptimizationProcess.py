
# Carga de librerias

from src.app import Training
from src.app import DataWrangling
import numpy as np
import pandas as pd

# Definición de variables globales

data_store = None
data = None
informe = None
df_cols = None

# Ejecucion el proceso de optimización

def Optimizar(df):
    df_prepared = PrepararDatos(df)
    proceso = Entrenar(df_prepared)
    ModelConverter()
    return proceso

# Convierte el dataset en un dataframe para poder manejar la informacion de forma mas sencilla y limpia los datos 

def PrepararDatos(dataset):     
    global data_sales,data_store,data,df_sales,df_cols
    for file in dataset:
        if str(file) == 'sales.csv':

            diclist = {"product_id": object,"store_id": object,"date": object, "sales":float, "revenue": float, "stock":float, "price":float,"promo_type_1":object, "promo_bin_1":object,"promo_type_2":object, "promo_bin_2":object, "promo_discount_2":object, "promo_discount_type_2": object }                                        
            data_sales = pd.read_csv(file, dtype= diclist, sep= ",")
            data_sales = DataWrangling.DateTransform(data_sales)
            

            moda = data_sales['product_id'].mode().to_list()
            moda = ' '.join(moda)
            data_sales = data_sales[data_sales['product_id'] == moda]
            data_sales = data_sales[data_sales['store_id'] == 'S0001']

            data_sales = data_sales.set_index('date')
            data_sales = data_sales.asfreq('D')
            data_sales = data_sales.sort_index()

            print(data_sales.head())
 
            df_sales = DataWrangling.Preprocesar(data_sales)
            print("df despues de data wrangling")
            print(df_sales.head())

            df_cols = df_sales[['product_id','store_id','sales','stock','price','promo_type_1','promo_type_2','promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2']]

            df_sales_final = df_sales.drop(columns=['promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2'])

            print(df_sales_final.head())

        elif str(file) == 'store_cities.csv':
            data_store = pd.read_csv(file)
    
    data = pd.merge(df_sales_final,data_store, on=['store_id'])     # une tabla sales y store por id de tienda

    return df_sales_final

# Entrena el modelos con los datos preparados   

def Entrenar(df):
    global informe,df_sales,df_cols

    # Aqui se obtienen los datos de la predicción y las métricas del algoritmo escogido
    modelo, informe = Training.TrainModel(df)

    modelo = np.round(modelo,2)

    # Copia de las predicciones en nuevos registros
    
    tam = len(modelo)   # esta variable determina el número de registros nuevos a generar 
    #tam = 100  
    while tam:
        print('modelo:',tam,'sample:',df_cols)
        new_row  = df_cols.iloc[tam]
        new_row.index.names = modelo.index.name  
        new_row.at['revenue'] =  modelo[tam]
        print(new_row)

        df_sales =pd.concat([df_sales,new_row.to_frame().T], ignore_index=True)
        tam-=1
    
    print(df_sales.tail())

    return True

# Convierte de vuelta a formato csv los archivos usados y se comprimen para reducir el tamaño de archivo

def ModelConverter():
    global df_sales
    df_sales.to_csv("..\\dataset\\sales.csv", index=False, float_format='%.2f')     # , encoding='utf-8-sig'

# Prepara los datos para el informe de estadísticas en la aplicación 

def ObtenerEstadisticas():
    resultado = informe
    return resultado
