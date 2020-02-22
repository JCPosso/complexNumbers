import unittest
from LibVectoresyMatricesComplejas import *
class TestMathMethods(unittest.TestCase):
        
        def test01_simularCircuito(self):
                x=matriz([ [[0,0],[1,0]],[[1,0],[0,0]] ])
                m= matriz( [ [[1,0],[1,0]],[[1,0],[-1,0]] ])
                c1=complejo(1/math.sqrt(2),0)
                h=m.multiplicaEscalar(c1)
                v0=matriz([ [[1,0]],[[0,0]] ] )
                v1=matriz([ [[1,0]],[[0,0]] ])
                v00=v0.productoTensor(v1)
                m1=x.productoTensor(h)
                m2=h.productoTensor(h)
                self.assertEqual(str((m2).multiplica(m1).multiplica(v00)),"[ 0.7071067811865474 ]\n[ 0 ]\n[ -0.7071067811865474 ]\n[ 0 ]\n")
        def test01_cambiarEstado(self):
                bol=matriz(
                            [[ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                            [ [0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                            [ [0,0],[1,0],[0,0],[0,0],[0,0],[1,0] ],
                            [ [0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                            [ [0,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                            [ [1,0],[0,0],[0,0],[0,0],[0,0],[0,0] ] ] )
                vector = matriz( [ [[0,0]],[[0,0]],[[0,0]],[[0,0]],[[0,0]],[[1,0]] ])
                self.assertEqual(str(bol.state(vector,2019)),"w")
        def test02_cambiarEstado(self):
                bol=matriz([[ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                              [ [0,0],[1,0],[0,0],[0,0],[0,0],[1,0] ],
                              [ [0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                              [ [1,0],[0,0],[0,0],[0,0],[0,0],[0,0] ] ] )
                xi=matriz([ [[6,0]],[[0,0]],[[3,0]],[[5,0]],[[3,0]],[[8,0]] ])
                self.assertEqual(str(bol.state(xi,5000)),"")
        def test03_cambiarEstado(self):
                bol=matriz([[ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                              [ [0,0],[1,0],[0,0],[0,0],[0,0],[1,0] ],
                              [ [0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                              [ [0,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                              [ [1,0],[0,0],[0,0],[0,0],[0,0],[0,0] ] ] )
             
                xi=matriz([ [[6,0]],[[5,0]],[[4,0]],[[3,0]],[[2,0]],[[1,0]] ])
                self.assertEqual(str(bol.state(xi,3000)),"")
        def test01_combinarMatrices(self):
                pos=matriz(     [[ [0,0],[1/6,0],[5/6,0] ],
                                [ [1/3,0],[1/2,0],[1/6,0] ],
                                [ [2/3,0],[1/3,0],[0,0] ] ])
                per=matriz([[ [1/3,0],[2/3,0] ],
                            [ [2/3,0],[1/3,0] ] ])
                epos=matriz([ [[1,0]],[[0,0]],[[0,0]] ])
                eper=matriz([ [[4/5,0]],[[1/5,0]]])       
                self.assertEqual(str(matriz.combinar(pos,per,epos,eper,0)),"")
        
if __name__ == '__main__':
	unittest.main()
