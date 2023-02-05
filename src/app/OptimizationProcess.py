
# Carga de librerias

from src.app import Training
from src.app import DataWrangling
import numpy as np
import pandas as pd

# Definición de variables globales

informe = None
df_cols = None
df_copia = None
df_copia_final = None

# Ejecucion el proceso de optimización

def Optimizar(df, producto):
    df_prepared = PrepararDatos(df, producto)
    if df_prepared.empty != True:
        proceso = Entrenar(df_prepared,producto)
        ModelConverter()
    return proceso

# Convierte el dataset en un dataframe para poder manejar la informacion de forma mas sencilla y limpia los datos 

def PrepararDatos(dataset, producto):     
    global data_sales,df_sales,df_cols, df_copia


    diclist = {"product_id": object,"store_id": object,"date": object, "sales":float, "revenue": float, "stock":float, "price":float,"promo_type_1":object, "promo_bin_1":object,"promo_type_2":object, "promo_bin_2":object, "promo_discount_2":object, "promo_discount_type_2": object }  

    # Lectura del dataset y creación del dataframe con los datos

    print("Empezando carga de dataset")
    data_sales = pd.read_csv(dataset, dtype= diclist, sep= ",")

    # Creación de la columna predicted

    print("Creando columna de prediccion")

    data_sales['predicted'] = 0
    data_sales['predicted'] = data_sales['predicted'].astype('int64')

    # Elimino fechas que no tienen dato (Solo para caso de uso)

    
    data_sales = DataWrangling.DateTransform(data_sales)

    print("Filtrando fechas en dataset original")

    data_sales = data_sales[data_sales.date < '2019-11-01']             # Elimino fechas sin datos 
    data_sales['date'] = data_sales['date'].dt.strftime('%Y-%m-%d')     # Vuelvo a convertir en string 
    

    # Limpieza de la copia del dataset original que se va a mantener

    print("Creando copia del dataset original")
   
    df_copia = DataWrangling.Preprocesar(data_sales)

    # Transformación de la columna date a datetime 

    print("Convirtiendo fechas")

    data_sales = DataWrangling.DateTransform(data_sales)

    print("Quitando columna de tienda")

    df_sales_final = data_sales.drop(columns=['store_id'])
  
    # Aqui se filtra en el dataset el producto deseado y una de las tiendas

    print("Filtrando producto")

    data_sales = data_sales[data_sales['product_id'] == producto]

    cantidad = len(data_sales)

    if cantidad < 50:
        return pd.DataFrame()

    # Guarda las columnas para las nuevas predicciones que se van a generar

    df_cols = data_sales[['product_id','store_id','sales','stock','price','promo_type_1','promo_type_2','promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2','date','predicted']]

    # Se realiza el proceso de limpieza en el dataset que solo contiene el producto seleccionado

    print("Limpiando datos que se van a utilizar")

    df_sales = DataWrangling.Preprocesar(data_sales)

    # Establece la columna fecha como índice de cada fila crea una frecuencia diaria, además de que ordena el índice

    print("Creando serie temporal a partir de columna de fechas")
   
    df_sales = df_sales.set_index('date')
    df_sales = df_sales.sort_index()
    
    # Se quitan las columnas innecesarias para entrenar el modelo

    df_sales_final = df_sales.drop(columns=['promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2'])

    return df_sales_final

# Entrena el modelos con los datos preparados   

def Entrenar(df,producto):
    global informe,df_sales,df_cols,df_copia,df_copia_final

    # Se obtienen los datos de la predicción y las métricas del algoritmo escogido

    print("Comenzando entrenamiento")

    modelo, informe = Training.TrainModel(df)

    # Se redondean los resultados obtenidos en el modelo 
    modelo = np.round(modelo,2)

    print(modelo)

    # Copia de las predicciones en nuevos registros
    # Creación del nuevo dataframe donde se van a copiar las predicciones

    copia = pd.DataFrame()

    tam = len(modelo)   # esta variable determina el número de registros nuevos a generar 
    i = 0
    while tam > i:
        print('modelo:',tam)
        df_cols = df_cols[df_cols['product_id'] == producto]
        new_row  = df_cols.iloc[i]
        new_row.at['date'] = modelo.index[i]
        new_row['date'] = new_row['date'].strftime('%Y-%m-%d')
        new_row.at['revenue'] =  modelo[i]
        new_row.at['predicted'] = int(1)

        print(new_row)

        copia = copia.append(new_row)
        i+=1
    print(copia)
    
    # Unión del dataframe original con el que contiene las predicciones

    df_copia_final =pd.concat([df_copia,copia], ignore_index=True)

    print(' Generando últimos registros')

    print(df_copia_final.tail())

    return True


# Convierte de vuelta a formato csv los archivos usados y se comprimen para reducir el tamaño de archivo

def ModelConverter():
    global df_copia_final

    print("Creando copia con los nuevos datos")

    df_copia_final.to_csv("..\\dataset\\sales.csv", index=False, float_format='%.2f')     # , encoding='utf-8-sig'



# Prepara los datos para el informe de estadísticas en la aplicación 

def ObtenerEstadisticas():
    resultado = informe
    return resultado
