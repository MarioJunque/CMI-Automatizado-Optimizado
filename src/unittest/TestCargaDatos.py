

import src.app.CargaDatos as cargaDatos
import numpy as np
import pandas as pd
import unittest


class TestCargaDatos(unittest.TestCase):
    
    def test_cargaCSV(self):
        data_path= "../../dataset/data_sample_ventas.csv"
        archivoCSV = cargaDatos.CargaCSV(data_path)
        self.assertEqual(1,archivoCSV.head())
        



if __name__ == '__main__':
    unittest.main()