import math;
from Lib import *    
"""Librería computación Cuántica: Números complejos
   librería para hacer operaciones entre vectores y matrices de  complejos.
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class matrizComplejo:
        def __init__(self,c):
            self.c=c
            for i in range(len(self.c)):
                for j in range(len(self.c[0])):
                        self.c[i][j]=complejo(self.c[i][j][0],self.c[i][j][1])
            
        def sumaVectores(self,W):
            #suma de dos vectores de complejos
             i=0
             res=matrizComplejo([[[0,0]]*len(self.c[i])])
             for j in range(len(self.c[i])):
                 res.c[i][j]=(self.c[i][j]).suma(W.c[i][j])
             print(res)
        
        def __str__(self):
              for i in range(len(self.c)):
                      for j in range(len(self.c[0])):
                              print(self.c[i][j])
              return""  
                
