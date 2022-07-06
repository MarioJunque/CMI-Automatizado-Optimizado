
def Limpieza(df):
    df.dropna() # Limpieza de datos Nan que no aportan ninguna información, aqui los cambios no se hacen efectivos en el dataset todavía
    df.drop_duplicates()  # También duplicados
    return df 
