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
            if(len(self.c[0])==len(other.c[0])and len(self.c)==len(other.c)):
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                            if isinstance(other.c[j][k], complejo):
                                    if(self.c[j][k].real != other.c[j][k].real or self.c[j][k].img != other.c[j][k].img):return False
            return True

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
        def instanciar(self):
             v2=matriz.iniciar(len(self.c),len(self.c[0]))
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                            v2.c[j][k]=self.c[j][k]
             return v2
        
        def suma(self,W):
             m=len(self.c);n=len(self.c[0]);n2=len(W.c);p=len(W.c[0])
             if(m!=n2 or n!=p):return( "Las matrices no tienen el tamaño apropiado") 
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
             if(isinstance(self,complejo)):temp=e;e=self;self=temp
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
             return "no ingresó un vector, intente nuevamente!"
        
        def productoInterno(self,W):
                producto= (self.adjunta() ).multiplica(W)
                if( len(self.c[0])==len(W.c[0])==1):
                        return producto
                return producto.trace()

        def isHermitian(self):
                n=matriz.instanciar(self)
                if( self==n.adjunta()):
                               return True
                return False
        
        def isUnitary(self):
             n=matriz.instanciar(self)
             if(len(self.c[0])==len(self.c)):
                     if( self.multiplica(n.adjunta())==(self.adjunta().multiplica(n) )):
                             return True
             return False

        def norma(self):
                m= matriz(self.c)
                return round(math.sqrt(int(str(self.productoInterno(m)))),2)

        def distancia(self,v2):
                return (self.suma( v2.inversa()).norma( ))

        
        def productoTensor(self,B):
                matrix=matriz.iniciar(len(B.c)*len(self.c),len(self.c[0])*len(B.c[0]))
                o=0;p=0
                for m in range(len(self.c)):
                        for n in range(len(self.c[0])):
                                for j in range(len(B.c)):
                                        for k in range(len(B.c[0])):
                                                if(o<len(matrix.c)):
                                                        if(p>=len(matrix.c[0])):
                                                                p=0;o+=1
                                                        matrix.c[o][p]=self.c[m][n].multiplica(B.c[j][k])
                                                        p+=1
                return matrix

        
        def __str__(self):
             s=""
             for j in range(len(self.c)):
                     s+="[ "
                     for k in range(len(self.c[0])):
                              s+=str(self.c[j][k])+" "
                     s+=']\n'
             return s
