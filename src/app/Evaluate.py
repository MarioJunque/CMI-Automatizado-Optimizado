from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Función para generar las predicciones 

def Predicciones(mod,datos_test):
    pred = pd.Series(mod.forecast(44))
    r2 = np.abs(r2_score(datos_test, pred))
    return pred,r2

# Función para generar las estadísticas que ve el usuario en la GUI

def Report(datos, modelo):
    pred = pd.Series(modelo.forecast(44))
    r2 = np.abs(r2_score(datos, pred))
    mse = mean_squared_error(datos, pred)
    rmse = np.sqrt(mse)
    informe = {'mse':mse, 'rmse': rmse, 'r2': r2}
    return informe
    


