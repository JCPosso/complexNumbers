#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math;
from LibreriaNumerosComplejos import *
import numpy as np
from numpy import linalg as al
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
                                                if(round(self.c[j][k].real,4) != round(other.c[j][k].real,4) or round(self.c[j][k].img,4) != round(other.c[j][k].img,4)):
                                                        return False
                        return True
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
                if(len(vector.c[0])==1 ):
                        res=matriz.iniciar(len(vector.c),1)
                        for j in range(len(self.c)):
                                for k in range(len(self.c[0])):
                                        res.c[j][0] =res.c[j][0].suma( self.c[j][k].multiplica(vector.c[k][0]) )
                        return res
                return "no ingresó un vector, intente nuevamente!"
        
        def productoInterno(self,W):
                producto= (self.adjunta() ).multiplica(W)
                if( len(self.c[0])==len(W.c[0])==1):
                        return producto
                return producto.trace()

        def isHermitian(self):
                n=matriz.instanciar(self)
                for j in range(len(self.c)):
                            for k in range(len(self.c[0])):
                                    if( self.c[j][k]!=n.c[k][j].conjugado()):
                                            return False
                return True
        
        def isUnitary(self):
                n=matriz.instanciar(self)
                if(len(self.c[0])==len(self.c)):
                        if( self.multiplica(n.adjunta())==(self.adjunta().multiplica(n) )):
                                return True
                return False

        def norma(self):
                m= matriz(self.c)
                return math.sqrt(self.productoInterno(m).real)

        def distancia(self,v2):
                return (self.suma( v2.inversa()).norma( ))

        
        def productoTensor(self,B):
                f=len(B.c)*len(self.c)
                c=len(self.c[0])*len(B.c[0])
                matrix=matriz.iniciar(f,c)
                o=0;p=0
                for j in range(len(matrix.c)):
                        for k in range(len(matrix.c[0])):
                                matrix.c[j][k]=self.c[j//len(B.c)][k//len(B.c[0])].multiplica(B.c[j%len(B.c)][k%len(B.c[0])])
                return matrix
        def potencia(self,n):
                if(n==1):
                        return self
                else:
                        if( (n%2)==0):
                                return (self.potencia(n//2)).multiplica(self.potencia(n//2))
                        else:
                                return (self.potencia(n//2).multiplica(self.potencia(n//2))).multiplica(self)

        def state(self,v,times):
                if(times==0):return self
                return (self.potencia(times)).alcanceSobre(v)
        
        def combinar(m1,m2,v1,v2,n):
                if (n==0):
                        e1=v1
                        e2=v2
                else:
                        e1=m1.potencia(n).multiplica(v1)
                        e2=m2.potencia(n).multiplica(v2)
                return e1.productoTensor(e2)
        def cuadrada(self):
                return len(self.c)==len(self.c[0])
        def n_BlancosOptimo(n,n2):
                return n+( ((n//2)+1)*(n2-1))
        def isDoublyStochastic(self):
                vPrueba=matriz.iniciar(len(self.c),1)
                for i in range(len(self.c)):
                        vPrueba.c[i][0]=complejo(1,0)
                        
                return self.alcanceSobre(vPrueba)==vPrueba
        def eigen(self):
                a=[]
                for i in range(len(self.c)):
                        a.append([ [0,0] ]*len(self.c[0]))
                for i in range(len(a)):
                        for h in range(len(a[0])):
                                a[i][h]=complex(self.c[i][h].real,self.c[i][h].img)
                ob= np.array(a)
                eig_valu, eig_vect= al.eig(ob)
                

                vectores=[]
                for i in range(len(eig_vect)):
                        vectores.append(matriz.iniciar(len(eig_vect[0]),1))
                for i in range(len(vectores)):
                        for j in range(len(vectores[0].c)):
                                vectores[i].c[j][0]=complejo(eig_vect[i][j].real,eig_vect[i][j].imag)
                                
                        
                e_val=matriz.iniciar(len(eig_valu),1)
                for i in range(len(e_val.c)):
                                e_val.c[i][0]=complejo(eig_valu[i].real,eig_valu[i].imag)
                                
                return  e_val, vectores
        def __str__(self):
                s=""
                if isinstance(self,matriz):
                        for j in range(len(self.c)):
                                s+="[ "
                                for k in range(len(self.c[0])):
                                        s+=str(self.c[j][k])+" "
                                s+=']\n'
                return s
