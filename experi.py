import math;
from LibVectoresyMatricesComplejas import *
class experimentos(matriz):
    def marbles(self):
        m=input("por favor ingrese una matriz cuadrada booleana",end="")
        if(m.esCuadrada()):
            m=matriz(m)
            e0=input("por favor ingrese un estado en forma vectorial",end="")
            if(len(m.c)):
