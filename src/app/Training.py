from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor, ElasticNet

from skforecast.ForecasterAutoreg import ForecasterAutoreg
from skforecast.ForecasterAutoregCustom import ForecasterAutoregCustom
from skforecast.ForecasterAutoregDirect import ForecasterAutoregDirect
from skforecast.model_selection import grid_search_forecaster
from skforecast.model_selection import backtesting_forecaster

from src.app import Evaluate

# Ahora entrenamos nuestro modelo, pero para datos reales en lugar de usar samples

def TrainModel (datos):
    print(datos)  

    steps = 90
    datos_train = datos[:-steps]
    datos_test  = datos[-steps:]
    # Crear y entrenar forecaster autoregresivo recursivo
    # ==============================================================================
    forecaster = ForecasterAutoreg(
                 regressor = RandomForestRegressor(random_state=123),
                 lags = 6
             )

    forecaster = forecaster.fit(y=datos_train['revenue'])

    elegido = Evaluate.Predicciones(forecaster, datos_test)
    informe = Evaluate.Report(datos_test, elegido)

    return elegido, informe


#    lr =LinRegression(x_train,y_train)    
#    sgd = SGD_Reg(x_train,y_train)
#    en = Elastic(x_train,y_train)



#--------------------------------------------------------------------------------------------------

# Crear y entrenar forecaster
# ==============================================================================
#forecaster = ForecasterAutoreg(
#               regressor = RandomForestRegressor(random_state=123),
#               lags      = 8
#            )

#forecaster.fit(y=datos_train['y'], exog=datos_train['exog_1'])

#--------------------------------------------------------------------------------------------------



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
