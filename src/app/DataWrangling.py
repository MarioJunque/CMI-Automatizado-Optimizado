import numpy as np
import pandas as pd
from scipy import stats

# Coordina el proceso de Limpieza de datos del dataset

def Preprocesar(df):
    df = LimpiezaDeDatos(df)
    df = DateTransform(df)
    df_final = EliminarDuplicados(df)
    return df_final

# Elimina o sustituye los valores nulos del dataset

def LimpiezaDeDatos(df):
    df_numeric = df[["sales","price", "revenue", "stock"]]
    for i in df_numeric.columns:
        col = df_numeric[i]
        media = np.mean(col)
        col.fillna(media, inplace=True)
        df[i] = col
        print(df[i])
    return df

# Comprueba si hay registros duplicados, si los hay los elimina

def EliminarDuplicados(df):
    if (len(df) == len(df.drop_duplicates())) == False:
        df.drop_duplicates()
    return df 

# Se encarga de realizar las transformaciones necesarias para el correcto funcionamiento del modelo 

def DateTransform(df):
# Tambien se transforma a enteto las ventas y el stock 
    df[['sales','stock']] = df[['sales','stock']].astype('int')

# Convierte las fechas en formato object a formato datetime 
    if df['date'].dtype != 'datetime64':
        df['date'] =  pd.to_datetime(df['date'])

    return df  

# Elimina posibles outliers que puedan repercutir en el modelo de entrenamiento

def FiltroDeOutliers(df):
    df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

    #df[(np.abs(stats.zscore(df[0]) <3))]
    return df