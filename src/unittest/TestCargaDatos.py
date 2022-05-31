

from src.app.CargaDatos import CargaCSV as Load
import numpy as np
import pandas as pd
import unittest


class TestCargaData(unittest.TestCase):
    
    def test_cargaCSV(self):
        data_path= "../../dataset/data_sample_ventas.csv"
        df = Load(data_path).crearDataframe()
        self.assertFalse(0,df.empty)

    #def test_cargaXSLX(self):
    #    data_path= "../../dataset/superstore_sales.xlsx"
    #    archivoXSLX = Load.CargaXSLX(data_path)
    #    self.assertEqual(1,archivoXSLX)



if __name__ == '__main__':
    unittest.main()