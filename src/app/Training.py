from sklearn.ensemble import RandomForestRegressor

from scipy import stats
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.model_selection import grid_search_forecaster
from skforecast.utils import load_forecaster
from skforecast.utils import save_forecaster
from src.app import Evaluate
import os
import numpy as np


def TrainModel (datos):
    print(datos.index.freq)
    datos = datos.asfreq('D', fill_value=np.mean(datos['revenue']))
    datos_rev = datos['revenue']

    # Separación de los datos en conjunto de entrenamiento y test

    steps = 40
    datos_train = datos_rev[:-steps]
    datos_test  = datos_rev[-steps:]

    print("Conjunto de entrenamiento")
    print(datos_train.head())

    print("Conjunto de test")
    print(datos_test.head())

    if os.path.exists('../src/app/forecaster.py') == True:
        forecaster= load_forecaster('..\\src\\app\\forecaster.py', verbose=True)
        print('Forecaster cargado')
        prediccion = forecaster.predict(steps=steps, last_window=datos_rev.tail(12))
        print('New predictions')
        print(prediccion)
    else:
        # Crear y entrenar forecaster autoregresivo recursivo
        # ==============================================================================
        forecaster = ForecasterAutoreg(
                    regressor =  RandomForestRegressor(max_depth=2, n_estimators=300,random_state=123),
                    lags = 20
                )

        # Entrenamiento del modelo
        

        forecaster.fit(y=datos_train)

        # Evaluación del modelo

        test = Evaluate.Predicciones(forecaster, datos_test,steps)

        print(test)

        # Llamada a función ajustar en caso de necesitar ajustar el sistema 

        #ajustar(forecaster, datos_train)

        prediccion = forecaster.predict(steps=steps, last_window=datos_rev.tail(20))

    informe = Evaluate.Report(datos_test, forecaster,steps)

    # Aqui guardo el modelo actual
    guardarModelo(forecaster)

    return prediccion, informe

####################################################################################################################################


# Esta función prueba varios hiperparámetros para buscar la mejor combinación de estos
# para encontrar el mejor rendimiento del algoritmo

def ajustar(forecaster, datos_train):
    steps = 36
    forecaster = ForecasterAutoreg(
                    regressor = RandomForestRegressor(random_state=123),
                    lags      = 12 # Este valor será remplazado en el grid search
                )

    # Lags utilizados como predictores
    lags_grid = [5,10, 20]

    # Hiperparámetros del regresor
    param_grid = {'n_estimators': [100, 300, 500],
                'max_depth': [3, 5, 10]}

    resultados_grid = grid_search_forecaster(
                            forecaster         = forecaster,
                            y                  = datos_train,
                            param_grid         = param_grid,
                            lags_grid          = lags_grid,
                            steps              = steps,
                            refit              = True,
                            metric             = 'mean_squared_error',
                            initial_train_size = int(len(datos_train)*0.5),
                            fixed_train_size   = False,
                            return_best        = True,
                            verbose            = False
                    )
    print(resultados_grid)

# Este método guarda el modelo para que se pueda volver a usar posteriormente

def guardarModelo(modelo):
    save_forecaster(modelo, file_name='..\\src\\app\\forecaster.py', verbose=False)