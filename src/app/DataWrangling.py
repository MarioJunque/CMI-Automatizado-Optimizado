import numpy as np
import pandas as pd
from scipy import stats

# Coordina el proceso de Limpieza de datos del dataset

def Preprocesar(df):
    df = LimpiezaDeDatos(df)
    df = ReducirDimensiones(df)
    df = DateTransform(df)
    df_final = EliminarDuplicados(df)
    return df_final

# Elimina del dataset las dimensiones que no se van a usar para el entrenamiento del modelo

def ReducirDimensiones(df, detect):
    if detect == 1:
        df = df.drop(columns=['promo_bin_1','promo_bin_2','promo_discount_2','promo_discount_type_2'])
    elif detect == 2:
        pass
    return df


# Elimina o sustituye los valores nulos del dataset

def LimpiezaDeDatos(df):
    df_numeric = df["SALES","QUANTITYORDERED" "TOTALREVENUE","MSRP","DISCOUNTRATE"]
    for i in df_numeric:
        if df_numeric.iloc[i].isnull() == True:
            media = df.loc[df[i]]
            df["SALES"].replace("Nan",media)

    return df

# Comprueba si hay registros duplicados, si los hay los elimina

def EliminarDuplicados(df):
    if (len(df) == len(df.drop_duplicates())) == False:
        df.drop_duplicates()
    return df 

# Convierte las fechas en formato object a formato datetime

def DateTransform(df):
    df[['sales','stock']] = df[['sales','stock']].astype('int')
    if df['ORDER_DATE'].dtype != 'datetime':
        df[['ORDER_DATE']] =  pd.to_datetime(df['ORDERDATE'])
    return df  

# Elimina posibles outliers que puedan repercutir en el modelo de entrenamiento

def FiltroDeOutliers(df):
    df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]

    #df[(np.abs(stats.zscore(df[0]) <3))]
    return df