

import src.app.CargaDatos as Load
import numpy as np
import pandas as pd
import unittest


class TestCargaDatos(unittest.TestCase):
    
    def test_cargaCSV(self):
        data_path= "../../dataset/atp_matches_1997.csv"
        archivoCSV = Load.CargaCSV(data_path)
        print(archivoCSV)
        



if __name__ == '__main__':
    unittest.main()