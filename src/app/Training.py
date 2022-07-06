from sklearn.model_selection import train_test_split


# Ahora entrenamos nuestro modelo, pero para datos reales en lugar de usar samples

def TrainModelCV (X,Y):
    x_train,x_test,y_train,y_test= train_test_split(X,Y,test_size=0.3, random_state=0)
    return x_train,x_test,y_train,y_test