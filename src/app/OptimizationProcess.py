from src.app import Training
import pandas as pd

tabla_Orders= None
tabla_Returns= None
tabla_People= None
tabla_Final= None


archivoOptimizado = None

def PrepararDatos(dataset):
    global tabla_Orders, tabla_Returns, tabla_People, tabla_Final
    tabla_Orders = pd.read_excel(dataset, sheet_name=0, index_col=0)
    tabla_Returns = pd.read_excel(dataset, sheet_name=1, index_col=0)
    tabla_People = pd.read_excel(dataset, sheet_name=2, index_col=0)
    print(tabla_Orders)


def Entrenar():
    modelo = Training.TrainModelCV(tabla_Orders[['quantity']].values,tabla_Orders['profit'].values)
    tabla_Orders["prediccion"] = modelo
    return True
    

def Optimizar(df):
    PrepararDatos(df)
    proceso = Entrenar()
    ModelConverter()
    return proceso

def ModelConverter():
    df1= None
    with pd.ExcelWriter("..\\dataset\\superstore_sales.xlsx") as writer:
        tabla_Orders.to_excel(writer, sheet_name='Orders')
        tabla_Returns.to_excel(writer, sheet_name='Returns')
        tabla_People.to_excel(writer, sheet_name='People')
        writer.save()
