from statsmodels.tsa.arima.model import ARIMA
from src.app import Evaluate

import numpy as np
import pandas as pd

def TrainModel (datos):
  
    datos_rev = datos.revenue.resample('W').sum()

    # Estabilizamos la serie usando el logaritmo

    datos_log = np.log(datos_rev)
    datos_diff = np.diff(datos_log)

    # Después al usar el parámetro 'd' del modelo ARIMA para diferenciar la serie y hacerla estacionaria
    # con media y varianza constante

    # Separación de los datos en conjunto de entrenamiento y test 
   
    datos_train = datos_diff[:103]         # Datos de 2017 y 2018
    datos_test  = datos_diff[103:]         # Datos de 2019 con valor


    # Crear y entrenar modelo ARIMA ============================================================================== 
    
    arima_model = ARIMA(datos_train, order=(1,0,0),seasonal_order=(0, 1, 0, 52)) 

    # Entrenamiento del modelo
    
    model = arima_model.fit()

    # Evaluación del modelo

    test = Evaluate.Predicciones(model, datos_test)

    prediccion = pd.Series(model.forecast(52))

    # Ahora para las predicciones generadas hay que deshacer los cambios que se han hecho al utilizar el logaritmo
    # y la diferenciacion, en este última habrá que hacer la suma cumulativa tantas veces como diferenciaciones haya

    original = datos_log[0]   # Término original que hay que conservar antes de la diferenciacion

    y_pred_sum = np.cumsum(prediccion) + original
    prediction = np.exp(y_pred_sum)

    print(prediction)

    fechas_prediccion = pd.date_range(start=datos_rev.index[-1], periods=52, freq='W')
    prediction.index = fechas_prediccion

    print('Primeros datos de la prediccion')
    print(prediction.head())

    print('Ultimos datos de la prediccion')
    print(prediction.tail())

    # Generación de las métricas para la pantalla de consulta de estadísticas

    informe = Evaluate.Report(datos_test, model)

    return prediction, informe
