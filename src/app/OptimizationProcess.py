
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
df_copia = None
df_copia_final = None

# Ejecucion el proceso de optimización

def Optimizar(df):
    df_prepared = PrepararDatos(df)
    proceso = Entrenar(df_prepared)
    ModelConverter()
    return proceso

# Convierte el dataset en un dataframe para poder manejar la informacion de forma mas sencilla y limpia los datos 

def PrepararDatos(dataset):     
    global data_sales,data_store,data,df_sales,df_cols, df_copia

   

    diclist = {"product_id": object,"store_id": object,"date": object, "sales":float, "revenue": float, "stock":float, "price":float,"promo_type_1":object, "promo_bin_1":object,"promo_type_2":object, "promo_bin_2":object, "promo_discount_2":object, "promo_discount_type_2": object }                                        
    data_sales = pd.read_csv(dataset, dtype= diclist, sep= ",")
    data_sales['predicted'] = 0
    data_sales['predicted'] = data_sales['predicted'].astype('int64')
    df_copia = DataWrangling.Preprocesar(data_sales[data_sales['store_id'] == 'S0001'])
    data_sales = DataWrangling.DateTransform(data_sales)
    print(data_sales['predicted'].tail())
    

    moda = data_sales['product_id'].mode().to_list()
    moda = ' '.join(moda)
    data_sales = data_sales[data_sales['product_id'] == moda]
    data_sales = data_sales[data_sales['store_id'] == 'S0001']

     # Guarda las columnas para las nuevas predicciones

    df_cols = data_sales[['product_id','store_id','sales','stock','price','promo_type_1','promo_type_2','promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2','date','predicted']]


    data_sales = data_sales.set_index('date')
    data_sales = data_sales.asfreq('D')
    data_sales = data_sales.sort_index()

    print(data_sales.head())

    df_sales = DataWrangling.Preprocesar(data_sales)
    print("df despues de data wrangling")
    print(df_sales.head())

   
    df_sales_final = df_sales.drop(columns=['promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2'])

    return df_sales_final

# Entrena el modelos con los datos preparados   

def Entrenar(df):
    global informe,df_sales,df_cols,df_copia,df_copia_final

    # Aqui se obtienen los datos de la predicción y las métricas del algoritmo escogido
    modelo, informe = Training.TrainModel(df)

    modelo = np.round(modelo,2)

    # Copia de las predicciones en nuevos registros
    
    tam = len(modelo)   # esta variable determina el número de registros nuevos a generar 

    i = 0

    copia = pd.DataFrame()

    while tam > i:
        print('modelo:',tam)
        new_row  = df_cols.iloc[i]
        new_row.at['date'] = modelo.index[i]
        new_row['date'] = new_row['date'].strftime('%Y-%m-%d')
        new_row.at['revenue'] =  modelo.iloc[i]
        new_row.at['predicted'] = int(1)

        print(new_row)

        copia = copia.append(new_row)

        #df_copia =pd.concat([df_copia,new_row.to_frame().T], ignore_index=True)
        i+=1
    print(copia)
    
    df_copia_final =pd.concat([df_copia,copia], ignore_index=True)

    print(modelo)

    print('últimos registros')

    print(df_copia_final.tail())

    return True

# Convierte de vuelta a formato csv los archivos usados y se comprimen para reducir el tamaño de archivo

def ModelConverter():
    global df_copia_final
    df_copia_final.to_csv("..\\dataset\\sales.csv", index=False, float_format='%.2f')     # , encoding='utf-8-sig'

# Prepara los datos para el informe de estadísticas en la aplicación 

def ObtenerEstadisticas():
    resultado = informe
    return resultado
