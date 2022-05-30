import numpy as np
import pandas as pd


class CargaCSV:
    def __init__(self,csv_path):
        self.path = csv_path
        df=pd.read_csv(self.path, encoding='latin1')   
        return df

class CargaXSLX:
    def __init__(self,excel_path):
        df=pd.read_excel(excel_path)   
        return df