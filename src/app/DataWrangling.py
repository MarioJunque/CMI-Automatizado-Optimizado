import numpy as np
import pandas as pd


# Coordina el proceso de Limpieza de datos del dataset

def Preprocesar(df):
    df = EliminarDuplicados(df)
    df = LimpiezaDeDatos(df)
    df = FeatureEngineering(df)
    df_final = FiltroDeOutliers(df)

    return df_final

# Elimina o sustituye los valores nulos del dataset

def LimpiezaDeDatos(df):
    df_numeric = df[["sales","price", "stock"]]
    for i in df_numeric.columns:
        col = df_numeric[i]
        media = np.mean(col)
        media = np.round(media,2)
        df[i].fillna(media,inplace=True)
        #df[i] = col
    return df

# Comprueba si hay registros duplicados, si los hay los elimina

def EliminarDuplicados(df):
    if (len(df) == len(df.drop_duplicates())) == False:
        df.drop_duplicates()
    return df 

# Se encarga de realizar las transformaciones necesarias para el correcto funcionamiento del modelo 

def DateTransform(df):

# Convierte las fechas en formato object a formato datetime 
    if df['date'].dtype != 'datetime64':
        df['date'] =  pd.to_datetime(df['date'])

    return df  

# Transforma a entero las ventas y el stock 

def FeatureEngineering(df):
 
    df[['sales','stock']] = df[['sales','stock']].astype('int')
    return df

# Elimina posibles outliers que puedan repercutir en el modelo de entrenamiento

def FiltroDeOutliers(df):
    numeric = ["sales","price", "stock"]
    threshold=3
    

    for i in numeric:

        z_scores = (df[i] - df[i].mean()) / df[i].std()
        # Identitifica las filas que tienen outliers

        outliers = df[(np.abs(z_scores) > threshold)]

        # Quita las filas que tienen outliers del dataframe
        df = df[~df.index.isin(outliers.index)]

    return df