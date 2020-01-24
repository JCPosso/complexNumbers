import math;
from Lib import *    
"""Librería computación Cuántica: Números complejos
   librería para hacer operaciones entre vectores y matrices de  complejos.
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class matrizComplejo:
        def __init__(self,c,b):
            self.c = c[0]
            self.b=b
            
        def sumaVectores(self,V,W):
            #suma de dos vectores de complejos
             res=matrizComplejo([[0]*len(self.c[0])])
             for i in range(len(self.c[0])):
                 res.c[0][i]=V.c[0][i]+W.c[0][i]
                 print(res.c[0][i])
             return res
            
