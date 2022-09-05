from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection import cross_val_predict, cross_validate
import operator

# Se emplea validación cruzada (cross-validation) para hallar el error de fuera de la muestra 

dictR2={}
dictPredictions={}


def Eleccion():
    max_R2 = max(dictR2.items(), key=operator.itemgetter(1))
    return max_R2[0]


def Predicciones(x_test,mod,y_test):
    prediction = mod.predict(x_test)
    dictPredictions[mod] = prediction
    r2 = r2_score(y_test, prediction)
    dictR2[mod]= r2
    return prediction

def Report(x_test, y_test, modelo):
    prediction = modelo.predict(x_test)
    r2 = r2_score(y_test, prediction)
    mse = mean_squared_error(y_test, prediction)
    rmse = np.sqrt(mse)
    informe = {'mse':mse, 'rmse': rmse, 'r2': r2}
    return informe
    


