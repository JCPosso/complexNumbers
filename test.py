import unittest
from Lib import *
"""Librería computación Cuántica: Números complejos
   pruebaas de unidad a la libreria Py.py donde se evaluaran
   sus distintas propiedes y casos arbitrarios
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class TestMathMethods(unittest.TestCase):
    global a,b,c
    a=complejo(3,2)
    b=complejo(5,4)
    c=complejo(2,1)
    # Se evaluan las propiedades de la suma
    def test_suma(self):
        aa=a.suma(b)
        self.assertEqual(aa, complejo(8,6))
    def test_sumaEsConmutativa(self):
        aa=a.suma(b)
        bb= b.suma(a)
        self.assertEqual(aa,bb)
    def test_identidadDeSuma(self): 
        d= complejo(0,0)
        r=a.suma(d)
        self.assertEqual(r,a)

    # Se evaluan las propiedades de la resta
    def test_resta(self):
        x=a.resta(b)
        self.assertEqual(x, complejo(-2,-2))
    def test_restaNoEsConmutativa(self):
        x=a.resta(b)
        y= b.resta(a)
        self.assertFalse(x==y)
    def test_identidadDeResta(self): 
        d= complejo(0,0)
        r=a.resta(d)
        self.assertEqual(r,a)

    # Se evaluan las propiedades de la multiplicacion        
    def test_multiplicacion(self):
        x=a.multiplica(b)
        self.assertEqual(x,complejo(7,22))
    def test_multiplicacionPorCero(self):    
        d=complejo(0,0)
        x=a.multiplica(d)
        self.assertEqual(x,d) 
    def test_identidadDeMultiplicacion(self): 
        d=complejo(1,0)
        x=a.multiplica(d)
        self.assertEqual(x,a)

    # Se evaluan las propiedades de la division         
    def test_division(self):
        x=a.divide(b)
        self.assertEqual(x,complejo(0.56,-0.05))
    def test_identidadDeDivision(self): 
        d=complejo(1,0)
        x=a.divide(d)
        self.assertEqual(x,a)
    def test_divisionPorCero(self): 
        d=complejo(0,0)
        x=a.divide(d)
        self.assertEqual(x,"Divisor is zero!!")
        
    # Se evalua  modulo
    def test_modulo(self):
        r=a.modulo()
        self.assertEqual(r,(3.61))
        
    # Se evaluan la conversion de cartesiano a polar         
    def test_pasarAPolar(self):
        r=c.aPolar()
        self.assertEqual(r,complejo(2.24, 0.46))
    # Se evaluan fase de un numero complejo          
    def test_fase(self):
        r=b.fase()
        self.assertEqual(r,(0.67))


if __name__ == '__main__':
    unittest.main()
