from sklearn.metrics import mean_squared_error, r2_score, classification_report
import numpy as np
from sklearn.model_selection import cross_val_predict, cross_validate
import operator

# Se emplea validación cruzada (cross-validation) para hallar el error de fuera de la muestra 

dictR2={}
dictPredictions={}

def evaluacionLin(X, Y, alg):
  
    scores=cross_validate(alg, X, Y, cv=3)
    mediaCV = np.mean(scores) # aporta como resultado 𝑅^2
    # Esto aporta el valor predicho real de 𝑅^2, de esta manera medimos como de buenas son las predicciones de nuestro modelo una vez entrenado
    yhat=cross_val_predict(alg, X, Y, cv=3)
    algoritmo = "algoritmo" + alg
    #dictR2['algoritmo']= yhat

def eleccion():
    max_R2 = max(dictR2.items(), key=operator.itemgetter(1))
    return max_R2[0]


def predicciones(x_test,mod,y_test):
    prediction = mod.predict(x_test)
    dictPredictions[mod] = prediction
    #mse = mean_squared_error(y_test, predictions)
    #rmse = np.sqrt(mse)
    r2 = r2_score(y_test, prediction)
    dictR2[mod]= r2
    return prediction
    


