import math;
from LibVectoresyMatricesComplejas import *
class experimentos(matriz):
    def marbles():
        m=input("por favor ingrese una matriz cuadrada booleana\n").lstrip("[").rstrip("]")
        for i in range(m.lenght):
            if i=="[":
                pass
        print(m)
        if(m.esCuadrada()):
            e0=matriz(input("por favor ingrese un estado en forma vectorial\n"))
            if(len(m.c)==len(e0.c)):
               print("yes")
if __name__ == '__main__':
    experimentos.marbles()
