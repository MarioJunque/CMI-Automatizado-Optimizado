

import src.app.CargaDatos as Load
import numpy as np
import pandas as pd
import unittest


class TestCargaDatos(unittest.TestCase):
    
    def test_cargaCSV(self):
        data_path= "..\..\dataset\data_sample_ventas.csv"
        archivoCSV = Load.CargaCSV(data_path)
        print(archivoCSV.head())
        



if __name__ == '__main__':
    unittest.main()