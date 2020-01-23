import math;
from Lib import *    
"""Librería computación Cuántica: Números complejos
   librería para hacer operaciones entre vectores y matrices de  complejos.
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class matrizComplejo:
        def __init__(self,v):
            self.v = v
        def sumaVectores(self,V,W):
            #suma de dos vectores de complejos
             res=matrizComplejo([0]*len(self.v))
             for i in range(len(self.v)):
                 res.v[i]=V.v[i]+W.v[i]
                 print(res.v[i])
             return res
            
