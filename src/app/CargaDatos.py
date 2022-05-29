import numpy as np
import pandas as pd


class CargaCSV:
    def __init__(self,csv_path):
        df=pd.read_csv(csv_path)   
        return df

class CargaXSLX:
    def __init__(self,excel_path):
        df=pd.read_excel(excel_path)   
        return df