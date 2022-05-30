import numpy as np
import pandas as pd


class CargaCSV:
    def __init__(self,csv):
        self.csv = csv

    def crearDataframe(self):
        df=pd.read_csv(self.csv, encoding='iso-8859-1')   
        return df

class CargaXSLX:
    def __init__(self,excel_path):
        df=pd.read_excel(excel_path)   
        return df