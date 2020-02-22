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
        global V,W,X,zero,c1,c2,A,B,C,In
        c1=complejo(3,3)
        c2=complejo(7,5)
        zero=matriz([ [[0,0]],[[0,0]],[[0,0]]])
        In=matriz.unitaria(3)
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
            
        def test_MatrizMultiplicacionEsAsociativa(self):
                r1=(A.multiplica(B)).multiplica(C)
                r2=A.multiplica(B.multiplica(C))
                self.assertEqual(r1,r2)
        def test_MatrizMultiplicacionTiene_In_comoUnidad(self):
                r1=In.multiplica(A)
                self.assertEqual(r1,A)
        def test_MatrizMultiplicacionDistribuyeEnadicion(self):
                res1=A.multiplica(B.suma(C))
                res2=(A.multiplica(B)).suma(A.multiplica(C))
                self.assertEqual(res1,res2)
        def test_MatrizMultiplicacionDistribuyeMultiplicacionEscalar(self):
                res1=A.multiplica(B).multiplicaEscalar(c1)
                res2=A.multiplicaEscalar(c1).multiplica(B)
                self.assertEqual(res1,res2)
        def test_MatrizMultiplicacionTieneTranspuesta(self):
                res1=A.multiplica(B).transpuesta()
                res2=B.transpuesta().multiplica(A.transpuesta())
                self.assertEqual(res1,res2)
        def test02_alcance(self):
                A=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
                V=matriz([ [[3,2]],[[1,9]],[[3,2]]])
                self.assertEqual('[ -10+67i ]\n[ -71+63i ]\n[ -17+70i ]\n',str(A.alcanceSobre(V)))                   
        def test_MatrizMultiplicacionTieneConjugada(self):
                res1=A.multiplica(B).conjugada()
                res2=A.conjugada().multiplica(B.conjugada())
                self.assertEqual(res1,res2)
        def test_MatrizMultiplicacionTieneAdjunta(self):
                res1=A.multiplica(B).adjunta()
                res2=B.adjunta().multiplica(A.adjunta())
                self.assertEqual(res1,res2)
            
        def test01_productoInterno(self):
                Z=matriz([ [[4,2],[7,2],[5,6]],[[7,9],[1,9],[8,0]],[[2,1],[1,5],[5,2]] ])
                W=matriz([ [[0,2],[1,0],[2,6]],[[9,9],[1,9],[7,7]],[[7,8],[4,5],[0,2]] ])
                self.assertEqual('394+66i',str(Z.productoInterno(W)))
        def test02_productoInterno(self):
                Z=matriz([ [[5,2],[3,1],[6,6]],[[6,9],[1,9],[4,0]],[[7,1],[4,5],[3,2]] ])
                W=matriz([ [[1,2],[3,2],[1,6]],[[4,9],[7,9],[0,0]],[[7,1],[8,5],[3,2]] ])
                self.assertEqual('375-15i',str(Z.productoInterno(W)))
        def test03_productoInterno(self):
                Z=matriz([ [[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0]] ])
                W=matriz([ [[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0]],[[0,0],[0,0],[0,0]] ])
                self.assertEqual('0',str(Z.productoInterno(W)))
            
        def test01_norma(self):
                Z=matriz([ [[4,2]],[[9,9]],[[0,2]] ])
                self.assertEqual('13.64',str(Z.norma()))
        def test02_norma(self):
                Z=matriz([ [[4,2],[5,8],[1,2]],[[9,7],[1,7],[3,1]],[[4,1],[5,0],[9,2]] ])
                self.assertEqual('20.76',str(Z.norma()))
        def test03_norma(self):
                Z=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
                self.assertEqual('20.93',str(Z.norma()))
            
        def test01_distancia(self):
                Z=matriz([ [[9,2],[6,2],[6,6]],[[6,6],[1,9],[6,0]],[[7,1],[6,5],[3,6]] ])
                W=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
                self.assertEqual('12.12',str(Z.distancia(W)))
        def test02_distancia(self):
                V=matriz([ [[1,0]],[[1,9]],[[9,0]] ])
                W=matriz([ [[5,7]],[[8,6]],[[1,5]] ])
                self.assertEqual('14.56',str(V.distancia(W)))
        def test03_distancia(self):
                Z=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
                W=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
                self.assertEqual('0.0',str(Z.distancia(W)))

        def test01_hermitian(self):
                Z=matriz([ [[1,0],[0,1]],[[0,-1],[1,0]] ])
                self.assertTrue(Z.isHermitian())
        def test02_hermitian(self):
                Z=matriz([ [[2,0],[1,1]],[[1,-1],[3,0]] ])
                self.assertTrue(Z.isHermitian())
        def test03_hermitian(self):
                Z=matriz([ [[1,0],[4,8]],[[5,2],[4,0]] ])
                self.assertFalse(Z.isHermitian())
        
        def test01_unitaria(self):
                Z=matriz([ [[1,0],[1,1]],[[1,-1],[2,0]] ])
                self.assertTrue(Z.isUnitary())
        def test02_unitaria(self):
                Z=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
                self.assertFalse(Z.isUnitary())
        def test03_unitariaDebeSerCuadrada(self):
                Z=matriz([ [[1,2],[3,2],[3,2]],[[3,2],[7,1],[3,2]] ])
                self.assertFalse(Z.isUnitary())
        
        def test01_productoTensor(self):
                k=matriz([ [[2,0]],[[3,0]] ])
                c=matriz([ [[4,0]],[[6,0]],[[3,0]] ])
                self.assertEqual(str(k.productoTensor(c)),'[ 8 ]\n[ 12 ]\n[ 6 ]\n[ 12 ]\n[ 18 ]\n[ 9 ]\n')

        def test02_productoTensor(self):
                k=matriz([ [[1,0]],[[0,0]] ])
                b=matriz([ [[8,0]],[[0,0]],[[0,0]] ])
                c=matriz([ [[0,0]],[[6,0]] ])
                d=matriz([ [[0,0]],[[0,0]],[[3,0]] ])
                self.assertEqual(str((k.productoTensor(b)).suma(c.productoTensor(d))),'[ 8 ]\n[ 0 ]\n[ 0 ]\n[ 0 ]\n[ 0 ]\n[ 18 ]\n')
        def test_marbles(self):
                bol=matriz([  [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[1,0],[0,0],[0,0],[0,0],[1,0] ],
                              [ [0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                              [ [1,0],[0,0],[0,0],[0,0],[1,0],[0,0] ]
                              ])
                vector=matriz([ [[6,0]],[[2,0]],[[1,0]],[[5,0]],[[3,0]],[[10,0]] ])

                t2=bol.alcanceSobre(vector)
                print(t2)
                assert  True
                        
        ###VERIFICAR ENTRADAS
        def test_sumaMatricesTamañosIguales(self):
                v1= matriz([ [[1,2]],[[3,5]],[[6,8]] ])
                v2= matriz([ [[3,5]],[[6,8]] ])
                self.assertTrue('Las matrices no tienen el tamaño apropiado',v1.suma(v2))
        def test_multiplicacionMatricesTamaños(self):
                a1= matriz([ [[1,2],[3,5],[3,5]],[[6,8],[3,5],[4,5]],[[7,5],[6,8],[8,5]] ])
                a2= matriz([ [[1,2],[3,5],[3,5]],[[6,8],[3,5],[4,5]] ])
                self.assertTrue('Las matrices no tienen el tamaño apropiado',a1.multiplica(a2))
if __name__ == '__main__':
        unittest.main()
