# Aqui deben de ir transformaciones de features, encoding de features categoricas, joinings y otras tecnicas 
# para la preparación del preprocesamiento 


def Agrupaciones(df,grupo, consulta):
    if consulta == "top 10 sales":
        df.groupby(grupo)
        df["Top 10 Sales"]= df.loc[:,'Sales']    
    elif consulta == "":
        pass
   
    return df

