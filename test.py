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
        self.assertEqual(aa, str(complejo(8,6)))
    def test_sumaEsConmutativa(self):
        aa=a.suma(b)
        bb= b.suma(a)
        self.assertEqual(aa,bb)
    def test_identidadDeSuma(self): 
        d= complejo(0,0)
        r=a.suma(d)
        self.assertEqual(r,str(a))

    # Se evaluan las propiedades de la resta
    def test_resta(self):
        x=a.resta(b)
        self.assertEqual(x,str( complejo(-2,-2)))
    def test_restaNoEsConmutativa(self):
        x=a.resta(b)
        y= b.resta(a)
        self.assertFalse(x==y)
    def test_identidadDeResta(self): 
        d= complejo(0,0)
        r=a.resta(d)
        self.assertEqual(r,str(a))

    # Se evaluan las propiedades de la multiplicacion        
    def test_multiplicacion(self):
        x=a.multiplica(b)
        self.assertEqual(x,str(complejo(7,22)))
    def test_multiplicacionPorCero(self):    
        d=complejo(0,0)
        x=a.multiplica(d)
        self.assertEqual(x,str(d)) 
    def test_identidadDeMultiplicacion(self): 
        d=complejo(1,0)
        x=a.multiplica(d)
        self.assertEqual(x,str(a))

    # Se evaluan las propiedades de la division         
    def test_division(self):
        x=a.divide(b)
        self.assertEqual(x,str(complejo(0.56,-0.05)))
    def test_identidadDeDivision(self): 
        d=complejo(1,0)
        a=complejo(3.0,2.0)
        x=a.divide(d)
        self.assertEqual(x,str(a))
    def test_divisionPorCero(self): 
        d=complejo(0,0)
        x=a.divide(d)
        self.assertEqual(x,"Divisor is zero!!")
        
    # Se evalua  modulo
    def test01_modulo(self):
        r=a.modulo()
        self.assertEqual(r,(3.61))
    def test02_modulo(self):
        r=b.modulo()
        self.assertEqual(r,(6.4))
    def test03_modulo(self):
        r=c.modulo()
        self.assertEqual(r,(2.24))
        
    #se evalua el conjugado
    def test01_conjugado(self):
        r=a.conjugado()
        self.assertEqual(r,'3-2i')
    def test02_conjugado(self):
        r=b.conjugado()
        self.assertEqual(r,'5-4i')
    def test03_conjugado(self):
        r=c.conjugado()
        self.assertEqual(r,'2-i')
        
    # Se evaluan la conversion de cartesiano a polar         
    def test01_pasarAPolar(self):
        r=c.aPolar()
        self.assertEqual(r,complejo(2.24, 0.46))
    def test02_noPasarAPolarSiDivisorEsCero(self):
        d=complejo(0,0)
        x=d.aPolar()
        self.assertEqual(x,"NOT possible to convert!")
    def test03_pasarAPolar(self):
        r=b.aPolar()
        self.assertEqual(r,complejo(6.4, 0.67))
        
    # Se evaluan fase de un numero complejo          
    def test01_faseCuadrante2(self):
        b=complejo(-5,4)
        r=b.fase()
        self.assertEqual(r,'141.34°Grados')
    def test02_faseCuadrante3(self):
        c=complejo(-8,-5)
        r=c.fase()
        self.assertEqual(r,'212.01°Grados')
    def test03_faseCuadrante4(self):
        c=complejo(9,-2)
        r=c.fase()
        self.assertEqual(r,'347.47°Grados')
    def test04_noRetornarFaseSiEsIndefinido(self):
        c=complejo(0,0)
        r=c.fase()
        self.assertEqual(r,'indefinido!!')


if __name__ == '__main__':
    unittest.main()
