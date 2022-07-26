from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor, ElasticNet
from src.app import Evaluate


# Ahora entrenamos nuestro modelo, pero para datos reales en lugar de usar samples

def TrainModelCV (X,Y):
    x_train,x_test,y_train,y_test= train_test_split(X,Y,test_size=0.3, random_state=0)
    lr =LinRegression(x_train,y_train)    
    sgd = SGD_Reg(x_train,y_train)
    en = Elastic(x_train,y_train)

    # Pasamos a evaluar cada modelo
    #Evaluate.evaluacionLin(x_test,y_test,lr) 
    #Evaluate.evaluacionLin(x_test,y_test,sgd)
    #Evaluate.evaluacionLin(x_test,y_test,en)

    #Predicciones
    Evaluate.predicciones(x_test,lr)
    Evaluate.predicciones(x_test,sgd)
    Evaluate.predicciones(x_test,en)

    resultado = Evaluate.eleccion()
    elegido = None
    if resultado == 'lr':
         elegido = lr
    elif resultado == "sgd":
         elegido= sgd
    elif resultado == "en":
        elegido = en
    return elegido

def LinRegression(x_train,y_train):                     # Entrena usando regresión linear
    modelo = LinearRegression().fit(x_train,y_train)
    return modelo 


def SGD_Reg(x_train,y_train):                           # Entrena usando algoritmo de regresión SGD
    modelo = SGDRegressor().fit(x_train,y_train)       
    return modelo 

def Elastic(x_train,y_train):                           # Entrena usando algoritmo Elastic Net
    modelo = ElasticNet().fit(x_train,y_train)
    return modelo 
