import unittest
from LibVectoresyMatricesComplejas import *
"""Librería computación Cuántica: Números complejos
   pruebaas de unidad a la libreria Py.py donde se evaluaran
   sus distintas propiedes y casos arbitrarios
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class TestMathMethods(unittest.TestCase):
    ###Vector complejo espacial.
    global V,W,X
    V=matrizCompleja([ [[3,2]],[[1,9]],[[3,2]] ])
    W=matrizCompleja([ [[5,2]],[[4,1]],[[1,2]] ])
    X=matrizCompleja([ [[3,4]],[[6,8]],[[3,0]] ])   
    #Adicion
    def test_sumaEsConmutativa(self):
        r1=V.suma(W)
        r2=W.suma(V)
        self.assertEqual(r1,r2)
        
if __name__ == '__main__':
    unittest.main()

