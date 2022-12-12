from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import operator

dictR2={}
dictPredictions={}


def Eleccion():
    max_R2 = max(dictR2.items(), key=operator.itemgetter(1))
    return max_R2[0]


def Predicciones(mod,datos_test):
    steps = 90
    prediction = mod.predict(steps=steps)
    print(prediction)
    dictPredictions[mod] = prediction
    r2 = r2_score(datos_test['revenue'], prediction)
    dictR2[mod]= r2
    return prediction

def Report(datos, modelo):
    steps = 90
    prediction = modelo.predict(steps=steps)
    r2 = r2_score(datos['revenue'], prediction)
    mse = mean_squared_error(datos['revenue'], prediction)
    rmse = np.sqrt(mse)
    informe = {'mse':mse, 'rmse': rmse, 'r2': r2}
    return informe
    


