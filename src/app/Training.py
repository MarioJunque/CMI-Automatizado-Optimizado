from statsmodels.tsa.arima.model import ARIMA
from src.app import Evaluate

import numpy as np
import pandas as pd

def TrainModel (datos):
  
    datos_rev = datos.revenue.resample('W').sum()
    datos_disp = datos_rev.loc[:'2019-11-03']

    # Estabilizamos la serie usando el logaritmo

    datos_log = np.log(datos_disp)

    # Después al usar el parámetro 'd' del modelo ARIMA para diferenciar la serie y hacerla estacionaria
    # con media y varianza constante

    # Separación de los datos en conjunto de entrenamiento y test 
   
    steps = 44

    datos_train = datos_log.loc[:'01-01-2019']
    datos_test  = datos_log.loc['01-01-2019':]

    print("Conjunto de entrenamiento")
    print(datos_train.head())

    print("Conjunto de test")
    print(datos_test.head())

    # Crear y entrenar modelo ARIMA ============================================================================== 
    
    arima_model = ARIMA(datos_train, order=(1,1,2))

    # Entrenamiento del modelo
    
    model = arima_model.fit(y=datos_train)

    # Evaluación del modelo

    test = Evaluate.Predicciones(model, datos_test,steps)

    print(test)

    prediccion = pd.Series(model.forectast(52)[0], index = datos_log['2019-11-03':].index)

    # Ahora para las predicciones generadas hay que deshacer los cambios que se han hecho al utilizar el logaritmo
    # y la diferenciacion, en este última habrá que hacer la suma cumulativa tantas veces como diferenciaciones haya

    original = prediccion[0]   # Término original que hay que conservar antes de hacer el proceso inverso

    prediccion = np.cumsum(prediccion)
    
    prediccion = prediccion + original

    prediccion = np.exp(prediccion)

    # Generación de las métricas para la pantalla de consulta de estadísticas

    informe = Evaluate.Report(datos_test, model,steps)

    return prediccion, informe
