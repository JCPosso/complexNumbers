import unittest
from LibVectoresyMatricesComplejas import *
"""Librería computación Cuántica: Números complejos
   pruebaas de unidad a la libreria Py.py donde se evaluaran
   sus distintas propiedes y casos arbitrarios
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class TestMathMethods(unittest.TestCase):
    ###Operaciones en espacios vectoriales complejos.
    
    global V,W,X,zero,c1,c2,A,B,C
    c1=complejo(3,3)
    c2=complejo(7,5)
    zero=matriz([ [[0,0]],[[0,0]],[[0,0]]])

    
    #vecctores
    V=matriz([ [[3,2]],[[1,9]],[[3,2]] ])
    W=matriz([ [[5,2]],[[4,1]],[[1,2]] ])
    X=matriz([ [[3,4]],[[6,8]],[[3,0]] ])
    #matrices
    A=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
    B=matriz([ [[5,2],[7,6],[6,0]],[[3,1],[1,9],[0,5]],[[4,4],[6,8],[3,9]] ])
    C=matriz([ [[6,2],[3,9],[8,1]],[[2,9],[8,9],[3,1]],[[7,2],[9,5],[1,2]] ])

    def test_sumaEsConmutativa(self):
        r1=V.suma(W)
        r2=W.suma(V)
        self.assertEqual(r1,r2)
    def test_sumaEsAsociativa(self):
        r1=(V.suma(W)).suma(X)
        r2=V.suma((W).suma(X))
        self.assertEqual(r1,r2)
    def test_CeroEsIdentidadAditiva(self):
        r1=(V.suma(W)).suma(X)
        answ=r1.suma(zero)
        self.assertEqual(r1,answ)
    def test_VectorTieneInversa(self):
        answ=V.suma(V.inversa())
        self.assertTrue(answ,zero)
    def test_scalarMultiplicationHasUnit(self):
        answ=V.multiplicaEscalar(complejo(1,0))
        self.assertEqual(answ,V)
    def test_multiplicacionEscalarCumpleMultiplicacionCompleja(self):
        res1=matriz.multiplicaEscalar((matriz.multiplicaEscalar(V,c1)),c2)
        res2=matriz.multiplicaEscalar(V,c1.multiplica(c2))
        self.assertEqual(res1,res2)
    def test_sumaDistribuyeEnMultiplicacionEscalar(self):
        res1=V.multiplicaEscalar(c1.suma(c2))
        res2=(V.multiplicaEscalar(c1)).suma(V.multiplicaEscalar(c2))
        self.assertEqual(res1,res2)

##Operaciones en espacios matriciales complejas
    def test_transpuestaEsIdempotente(self):
        self.assertEqual( (A.transpuesta()).transpuesta(),A)
    def test_transpuestaRespectoAdicion(self):
        self.assertEqual( (A.suma(B)).transpuesta(),(A.transpuesta()).suma(B.transpuesta()))        
    def test_transpuestaRespectoMultiplicacionEscalar(self):
        self.assertEqual( (A.multiplicaEscalar(c1)).transpuesta(),A.transpuesta().multiplicaEscalar(c1))

    def test_conjugadoEsIdempotente(self):
        res1=A.conjugada().conjugada()
        self.assertEqual( res1,A)
    def test_conjugadoRespectoAdicion(self):
        res1=(A.suma(B)).conjugada()
        res2=A.conjugada().suma(B.conjugada())
        self.assertEqual( res1,res2)
    def test_conjugadoRespectoMultiplicacionEscalar(self):
        res1=(A.multiplicaEscalar(c1)).conjugada()
        res2=A.conjugada().multiplicaEscalar(c1.conjugado())
        self.assertEqual( res1,res2)


    def test_adjuntaEsIdempotente(self):
        res1=A.adjunta().adjunta()
        self.assertEqual( res1,A)
    def test_adjuntaRespectoAdicion(self):
        res1=(A.suma(B)).adjunta()
        res2=A.adjunta().suma(B.adjunta())
        self.assertEqual( res1,res2)
    def test_adjuntaRespectoMultiplicacionEscalar(self):
        res1=A.multiplicaEscalar(c1).adjunta()
        res2=A.adjunta().multiplicaEscalar(c1.conjugado())
        self.assertEqual( res1,res2)
        
if __name__ == '__main__':
    unittest.main()

