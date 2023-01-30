from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import operator

# Declaración de diccionario que contendrá el R^2 de cada algoritmo y el diccionario con el nombre de cada algoritmo

dictR2={}
dictPredictions={}

# Función para elegir el mejor algoritmo 

def Eleccion():
    max_R2 = max(dictR2.items(), key=operator.itemgetter(1))
    return max_R2[0]

# Función para generar las predicciones 

def Predicciones(mod,datos_test,steps):
    prediction = mod.predict(steps=steps)
    dictPredictions[mod] = prediction
    r2 = r2_score(datos_test, prediction)
    dictR2[mod]= r2
    return prediction,r2

# Función para generar las estadísticas que ve el usuario en la GUI

def Report(datos, modelo,steps):
    prediction = modelo.predict(steps=steps)
    r2 = r2_score(datos, prediction)
    mse = mean_squared_error(datos, prediction)
    rmse = np.sqrt(mse)
    informe = {'mse':mse, 'rmse': rmse, 'r2': r2}
    return informe
    


