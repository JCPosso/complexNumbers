import math;
from LibreriaNumerosComplejos import *    
"""Librería computación Cuántica: Números complejos
   librería para hacer operaciones entre vectores y matrices de  complejos.
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)rr
"""

class matriz:
        def __init__(self,c):
            self.c=c
            for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                        if(not(isinstance(self.c[j][k],complejo))):
                         self.c[j][k]=complejo(self.c[j][k][0],self.c[j][k][1])

        def __eq__(self, other):
            """Override"""
            for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                            if isinstance(other.c[j][k], complejo):
                                    return( self.c[j][k].real == other.c[j][k].real and self.c[j][k].img == other.c[j][k].img)
            return False

        def iniciar(f,c):
                m=[]
                for i in range(f):
                        m.append([ [0,0] ]*c)
                return matriz(m)
        def unitaria(c):
                m=[]
                temp=matriz.iniciar(c,c)
                for i in range(c):
                        temp.c[i][i]=complejo(1,0)
                return temp
        def trace(C):
                suma=complejo(0,0)
                for j in range(len(C.c[0])):
                        suma=suma.suma(C.c[j][j])
                return suma

        
        def suma(self,W):
             m=len(self.c);n=len(self.c[0]);n2=len(W.c);p=len(W.c[0])
             if(m!=n2 or n!=p): return "Las matrices no tienen el tamaño apropiado"
             res=matriz.iniciar(len(self.c),len(self.c[0]))
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                            res.c[j][k]=(self.c[j][k]).suma(W.c[j][k])
             return res
        
        def inversa(self):
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                      self.c[j][k]=(self.c[j][k]).multiplica(complejo(-1,0))
             return self

        def multiplica(self,W):
             m=len(self.c);n=len(self.c[0]);n2=len(W.c);p=len(W.c[0])
             if(n!=n2): return "Las matrices no tienen el tamaño apropiado"
             res=matriz.iniciar(len(self.c),len(W.c[0]))
             for j in range(m):
                    for k in range(p):
                        cont=complejo(0,0)
                        for h in range(n):
                                cont=cont.suma( (self.c[j][h]).multiplica(W.c[h][k]) )
                        res.c[j][k]=cont
             return res
        
        def multiplicaEscalar(self,e):
             res=matriz.iniciar(len(self.c),len(self.c[0]))
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                        res.c[j][k]=(self.c[j][k]).multiplica(e)
             return res
        
        def transpuesta(self):
                m=matriz.iniciar(len(self.c[0]),len(self.c))
                for j in range(len(self.c[0])):
                        for k in range(len(self.c)):
                                m.c[j][k]=self.c[k][j]
                self.c=m.c
                return self
                
        def conjugada(self):
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                        self.c[j][k]=self.c[j][k].conjugado()
             return self
        
        def adjunta(self):
             self=(self.transpuesta()).conjugada()
             return self
        
        def alcanceSobre(self,vector):
             if(len(vector[0])==1 ): 
                     res=vectorComplejo([[0,0]]*len(vector))
                     for j in range(len(self.c)):
                            for k in range(len(self.c[0])):
                                  res.c[k] =res.c[k].suma( self.c[j][k].multiplica(vector[k]) )
                     return res
             return "no es un vector!"
        
        def productoInterno(self,W):
                producto= (self.adjunta() ).multiplica(W)
                if( len(self.c[0])==len(W.c[0])==1):
                        return producto
                return producto.trace()
        
        def isHermitian(self):
             if( self!= self.conjugada()):
                               return "ISN´T HERMITIAN!"
             return self
        
        def isUnitary(self):
             if( self.multiplica(self.adjunta()) != self.adjunta().multiplica(self) ):
                               return "ISN´T UNITARY!"
             return self

        def norma(self):
                m= matriz(self.c)
                return round(math.sqrt(int(str(self.productoInterno(m)))),2)

        def distancia(self,v2):
                return (self.suma( v2.inversa()).norma( ))

        
        def __str__(self):
             s=""
             for j in range(len(self.c)):
                     s+="[ "
                     for k in range(len(self.c[0])):
                              s+=str(self.c[j][k])+" "
                     s+=']\n'
             return s
