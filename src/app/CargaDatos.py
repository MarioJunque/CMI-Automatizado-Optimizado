import numpy as np
import pandas as pd


class CargaCSV:
    def __init__(self,csv_path):
        self.csv_path = csv_path
        df=pd.read_csv(self.csv_path)   
        return df
