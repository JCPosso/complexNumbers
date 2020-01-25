import math;
from LibreriaNumerosComplejos import *    
"""Librería computación Cuántica: Números complejos
   librería para hacer operaciones entre vectores y matrices de  complejos.
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class vectorComplejo:
        def __init__(self,c):
            self.c=c
            for j in range(len(self.c)):
                        self.c[j]=complejo(self.c[j][0],self.c[j][1])
            
        def suma(self,W):
            #suma de dos vectores de complejos
             res=vectorComplejo([[0,0]]*len(self.c))
             for j in range(len(self.c)):
                 res.c[j]=(self.c[j]).suma(W.c[j])
             return res
        def resta(self,W):
            #suma de dos vectores de complejos
             res=vectorComplejo([[0,0]]*len(self.c))
             for j in range(len(self.c)):
                 res.c[j]=(self.c[j]).resta(W.c[j])
             return res
        def inversa(self):
            #suma de dos vectores de complejos
             for j in range(len(self.c)):
                 self.c[j]=(self.c[j]).multiplica(complejo(-1,0))
             return self
        def multiplicaEscalar(self,e):
                for j in range(len(self.c)):
                        self.c[j]=(self.c[j]).multiplica(complejo(e,0))
                return self
        def producto(self,v2):
                res=vectorComplejo([[0,0]]*len(self.c))
                for j in range(len(self.c)):
                        self.c[j]=(self.c[j]).multiplica(v2.c[j])
                return self
        def norma(self,v2):
                res=0
                for j in range(len(self.c)):
                        res+=(self.c[j]).multiplica(v2.c[j])
                return round(math.sqrt(res),2)
        def distancia(self,v2):
                res=0
                for j in range(len(self.c)):
                        res+=( (self.c[j]).resta(v2.c[j])).multiplica((self.c[j]).resta(v2.c[j]))
                return round(math.sqrt(res),2)
        
        def __str__(self):
                s=""
                for j in range(len(self.c)):
                              s+=str(self.c[j])+'\n'
                return s 
                
class matrizCompleja:
        def __init__(self,c):
            self.c=c
            for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                         self.c[j][k]=complejo(self.c[j][k][0],self.c[j][k][1])
        def iniciar(f,c):
                m=[]
                for i in range(f):
                        m.append([ [0,0] ]*c)
                return matrizCompleja(m)

        
        def suma(self,W):
            #suma de dos vectores de complejos
             """res= matrizCompleja.iniciar(len(self.c),len(self.c[0]))"""
             res=matrizCompleja.iniciar(len(self.c),len(self.c[0]))
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                            res.c[j][k]=(self.c[j][k]).suma(W.c[j][k])
             return res
        
        def inversa(self):
            #suma de dos vectores de complejos
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                      self.c[j][k]=(self.c[j][k]).multiplica(complejo(-1,0))
             return self
        
        def multiplicaEscalar(self,e):
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                        self.c[j][k]=(self.c[j][k]).multiplica(complejo(e,0))
             return self
        def transpuesta(self):
             cont=0   
             for j in range(len(self.c)):
                    cont+=1
                    for k in range(cont,len(self.c[0])):
                        temp=self.c[j][k]
                        self.c[j][k]=self.c[k][j]
                        self.c[k][j]=temp
                       
             return self
        
        def conjugada(self):
             for j in range(len(self.c)):
                    for k in range(len(self.c[0])):
                        self.c[j][k]=self.c[j][k].conjugado()
             return self
        def adjunta(self):
             self=(self.transpuesta()).conjugada()
             return self

        def alcanceSobre(self,vComplejo):
             if(isinstance(vComplejo ,vectorComplejo) ): 
                     res=vectorComplejo([[0,0]]*len(vComplejo))
                     for j in range(len(self.c)):
                            for k in range(len(self.c[0])):
                                  res.c[k] =res.c[k].suma( self.c[j][k].multiplica(vcomplejo[k]) )
                     return res
             return "no es un vector!"
        
        def __str__(self):
             s=""
             for j in range(len(self.c)):
                     s+="[ "
                     for k in range(len(self.c[0])):
                              s+=str(self.c[j][k])+" "
                     s+=']\n'
             return s 
