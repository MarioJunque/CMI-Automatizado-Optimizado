from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import pandas as pd

# Función para generar las predicciones 

def Predicciones(mod,datos_test):
    pred = pd.Series(mod.forecast()[0], index = datos_test.index)
    prediction = np.array(pred)
    r2 = r2_score(datos_test, prediction)
    return prediction,r2

# Función para generar las estadísticas que ve el usuario en la GUI

def Report(datos, modelo):
    pred = pd.Series(modelo.forecast()[0], index = datos.index)
    prediction = np.array(pred)
    r2 = r2_score(datos, prediction)
    mse = mean_squared_error(datos, prediction)
    rmse = np.sqrt(mse)
    informe = {'mse':mse, 'rmse': rmse, 'r2': r2}
    return informe
    


