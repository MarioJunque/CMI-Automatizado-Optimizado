# Aqui deben de ir transformaciones de features, encoding de features categoricas, joinings y otras tecnicas 
# para la preparación del preprocesamiento 

import pandas as pd


def Agrupaciones(df,grupo, consulta):
    if consulta == "top 10 sales":
        df["Top 10 Sales"]=  df.sort_values(str(grupo), ascending=False).iloc[:11]   
    elif consulta == "":
        pass
   
    return df


def transformarFecha(df):
    Anno = pd.DatetimeIndex(df["OrderDate"]).year
    Semana = pd.DatetimeIndex.isCalendar(df["OrderDate"]).week

