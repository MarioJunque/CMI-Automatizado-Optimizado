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
    Evaluate.Predicciones(x_test, lr, y_test)
    Evaluate.Predicciones(x_test, sgd, y_test)
    Evaluate.Predicciones(x_test, en, y_test) 

    resultado = str(Evaluate.Eleccion())
    elegido = None
    if resultado == 'LinearRegression()':
        elegido =  LinRegression(X,Y).predict(X)
        modeloElegido = lr
    elif resultado == "SGDRegressor()":
        elegido = SGD_Reg(X,Y).predict(X)
        modeloElegido = sgd
    elif resultado == "ElasticNet()":
        elegido =  Elastic(X,Y).predict(X)
        modeloElegido = en
    informe = Evaluate.Report(x_test, y_test, modeloElegido)
    print(informe)
    return elegido, informe

def LinRegression(x_train,y_train):                     # Entrena usando regresión linear
    modelo = LinearRegression().fit(x_train,y_train)
    return modelo 


def SGD_Reg(x_train,y_train):                           # Entrena usando algoritmo de regresión SGD
    modelo = SGDRegressor().fit(x_train,y_train)       
    return modelo 

def Elastic(x_train,y_train):                           # Entrena usando algoritmo Elastic Net
    modelo = ElasticNet().fit(x_train,y_train)
    return modelo 
