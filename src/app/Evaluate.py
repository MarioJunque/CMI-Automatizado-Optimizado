from sklearn.metrics import mean_squared_error, r2_score, classification_report
import numpy as np
from sklearn.model_selection import cross_val_predict, cross_validate

# Se emplea validación cruzada (cross-validation) para hallar el error de fuera de la muestra 

def evaluacionLin(lm, X, Y):
  
    scores=cross_validate(lm, X, Y, cv=3)
    mediaCV = np.mean(scores) # aporta como resultado 𝑅^2
    # Esto aporta el valor predicho real de 𝑅^2, de esta manera medimos como de buenas son las predicciones de nuestro modelo una vez entrenado
    yhat=cross_val_predict(lm, X, Y, cv=3)
    return yhat, mediaCV 


def predicciones(y_test,predictions):
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, predictions)
    return mse,rmse,r2