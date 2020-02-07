import unittest
from LibreriaNumerosComplejos import *
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
        def test_sumaEsAsociativa(self):
                r1= (a.suma(b)).suma(c)
                r2= a.suma((b).suma(c))
                self.assertEqual(r1,r2)
        def test_identidadDeSuma(self):
                d= complejo(0,0)
                r=a.suma(d)
                self.assertEqual(r,a)
        # Se evaluan las propiedades de la resta
        def test_resta(self):
                x=a.resta(b)
                self.assertEqual(x,complejo(-2,-2))
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
        def test_multiplicacionEsAsociativa(self):
                r1= (a.multiplica(b)).multiplica(c)
                r2= a.multiplica((b).multiplica(c))
                self.assertEqual(r1,r2)
        def test_multiplicacionEsConmutativa(self):
                aa=a.multiplica(b)
                bb= b.multiplica(a)
                self.assertEqual(aa,bb)
        def test_multiplicacionDistribuyeSobreAdicion(self):
                r1=a.multiplica(b.suma(c))
                r2=( a.multiplica(b)).suma(a.multiplica(c) )
                self.assertEqual(r1,r2)
        # Se evaluan las propiedades de la division
        def test_division(self):
                x=a.divide(b)
                self.assertEqual(x,complejo(0.56,-0.05))
        def test_identidadDeDivision(self):
                d=complejo(1,0)
                a=complejo(3.0,2.0)
                x=a.divide(d)
                self.assertEqual(x,a)
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
                self.assertEqual(str(r),'3-2i')
        def test02_conjugado(self):
                r=b.conjugado()
                self.assertEqual(str(r),'5-4i')
        def test03_conjugado(self):
                r=c.conjugado()
                self.assertEqual(str(r),'2-i')
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
                self.assertEqual(r,2.47)
        def test02_faseCuadrante3(self):
                c=complejo(-8,-5)
                r=c.fase()
                self.assertEqual(r,-2.58)
        def test03_faseCuadrante4(self):
                c=complejo(9,-2)
                r=c.fase()
                self.assertEqual(r,-0.22)
        def test04_noRetornarFaseSiEsIndefinido(self):
                c=complejo(0,0)
                r=c.fase()
                self.assertEqual(r,'indefinido!!')
if __name__ == '__main__':
        unittest.main()
