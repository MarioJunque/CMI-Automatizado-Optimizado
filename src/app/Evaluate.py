
from sklearn.model_selection import cross_val_score,cross_val_predict, cross_validate 
from sklearn import metrics
import numpy as np

# Se emplea validación cruzada (cross-validation) para hallar el error de fuera de la muestra 

def evaluacion(lm, X, Y, cv):
    scoring = ['precision_macro', 'recall_macro']
    scores=cross_validate(lm, X, Y, cv=3, scoring=scoring)
    sorted(scores.keys())
    m = lm.intercept_
    n = lm.coef_
    mediaCV = np.mean(scores) # aporta como resultado 𝑅^2
    # Esto aporta el valor predicho real de 𝑅^2, de esta manera medimos como de buenas son las predicciones de nuestro modelo una vez entrenado
    yhat=cross_val_predict(lm, X, Y, cv=3)
    return yhat, mediaCV, m , n, scores["test_recall_macro"],scores["test_precision_macro"]