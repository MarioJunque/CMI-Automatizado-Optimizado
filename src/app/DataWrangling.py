import FeatureEngineering as ft 


def Limpieza(df):
    df.dropna() # Limpieza de datos Nan que no aportan ninguna información, aqui los cambios no se hacen efectivos en el dataset todavía
    df.drop_duplicates()  # También duplicados
    df2 =ft.Agrupaciones(df)
    return df2
