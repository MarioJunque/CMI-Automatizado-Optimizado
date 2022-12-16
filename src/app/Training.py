from sklearn.ensemble import RandomForestRegressor

from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.model_selection import grid_search_forecaster
from skforecast.model_selection import backtesting_forecaster
from skforecast.utils import load_forecaster
from skforecast.utils import save_forecaster


from src.app import Evaluate
import os

# Ahora entrenamos nuestro modelo, pero para datos reales en lugar de usar samples

def TrainModel (datos):
    
    print(len(datos))
    steps = 90
    print(datos)
    datos_train = datos[:-steps]
    datos_test  = datos[-steps:]


    if os.path.exists('../src/app/forecaster.py') == True:
        forecaster= load_forecaster('..\\src\\app\\forecaster.py', verbose=True)
        print('Forecaster cargado')
        newpred =forecaster.predict(steps=3)
        print('New prediction')
        print(newpred)
    else:
        # Crear y entrenar forecaster autoregresivo recursivo
        # ==============================================================================
        forecaster = ForecasterAutoreg(
                    regressor = RandomForestRegressor(max_depth=5, n_estimators=500,random_state=123),
                    lags = 20
                )

    forecaster.fit(y=datos_train['revenue'])

    elegido = Evaluate.Predicciones(forecaster, datos_test)

    ajustar(forecaster, datos_train)

    informe = Evaluate.Report(datos_test, forecaster)


    guardarModelo(forecaster)

    return elegido, informe


#    lr =LinRegression(x_train,y_train)    
#    sgd = SGD_Reg(x_train,y_train)
#    en = Elastic(x_train,y_train)

    #Predicciones
#    Evaluate.Predicciones(x_test, lr, y_test)
#    Evaluate.Predicciones(x_test, sgd, y_test)
#    Evaluate.Predicciones(x_test, en, y_test) 

#     resultado = str(Evaluate.Eleccion())
#     elegido = None
#     if resultado == 'LinearRegression()':
#         elegido =  LinRegression(X,Y).predict(X)
#         modeloElegido = lr
#     elif resultado == "SGDRegressor()":
#         elegido = SGD_Reg(X,Y).predict(X)
#         modeloElegido = sgd
#     elif resultado == "ElasticNet()":
#         elegido =  Elastic(X,Y).predict(X)
#         modeloElegido = en
#     informe = Evaluate.Report(x_test, y_test, modeloElegido)
#     print(informe)
#     return elegido, informe

# def LinRegression(x_train,y_train):                     # Entrena usando regresión linear
#     modelo = LinearRegression().fit(x_train,y_train)
#     return modelo 


# def SGD_Reg(x_train,y_train):                           # Entrena usando algoritmo de regresión SGD
#     modelo = SGDRegressor().fit(x_train,y_train)       
#     return modelo 

# def Elastic(x_train,y_train):                           # Entrena usando algoritmo Elastic Net
#     modelo = ElasticNet().fit(x_train,y_train)
#     return modelo 

# Este método guarda el modelo para que se pueda volver a usar posteriormente


def ajustar(forecaster, datos_train):
    steps = 36
    forecaster = ForecasterAutoreg(
                    regressor = RandomForestRegressor(random_state=123),
                    lags      = 12 # Este valor será remplazado en el grid search
                )

    # Lags utilizados como predictoresnkj
    lags_grid = [10, 20]

    # Hiperparámetros del regresor
    param_grid = {'n_estimators': [100, 500],
                'max_depth': [3, 5, 10]}

    resultados_grid = grid_search_forecaster(
                            forecaster         = forecaster,
                            y                  = datos_train['revenue'],
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

def guardarModelo(modelo):
    save_forecaster(modelo, file_name='..\\src\\app\\forecaster.py', verbose=False)