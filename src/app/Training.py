from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, SGDRegressor, ElasticNet


# Ahora entrenamos nuestro modelo, pero para datos reales en lugar de usar samples

def TrainModelCV (X,Y):
    x_train,x_test,y_train,y_test= train_test_split(X,Y,test_size=0.3, random_state=0)
    lr =LinRegression(x_train,y_train)
    sgd = SGD_Reg(x_train,y_train)
    en = Elastic(x_train,y_train)


def LinRegression(x_train,y_train):
    modelo = LinearRegression().fit(x_train,y_train)
    return modelo 


def SGD_Reg(x_train,y_train):
    modelo = SGDRegressor().fit(x_train,y_train)
    return modelo 

def Elastic(x_train,y_train):
    modelo = ElasticNet().fit(x_train,y_train)
    return modelo 
