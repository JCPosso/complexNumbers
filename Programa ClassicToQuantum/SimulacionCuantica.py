#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import math;
from LibVectoresyMatricesComplejas import *
def make_matrix(tam_matriz,n_blancosPorRendija,n_rendijas,n_blancos , b_central,vector):
        ways= matriz.iniciar(tam_matriz,tam_matriz)
        rendija=1
        k=int(n_rendijas+b_central)
        flag=False
        for i in range( len(vector.c)):
                if(vector.c[i][0].img!=0):
                        flag=True
                        break
        #primera parte de llenado
        for i in range( 1, n_rendijas+1):
                if(flag):
                        ways.c[i][0].real=1/math.sqrt(n_rendijas)
                else:
                        ways.c[i][0].real=1/(n_rendijas)
        #segunda parte de llenado       
        while(k<len(ways.c)):
                ways.c[k][rendija]=vector.c[b_central-1][0]
                cont=1
                while(cont<n_blancosPorRendija):
                        if(cont%2!=0):
                                sig=(cont+1)//2                
                                ways.c[k-sig][rendija]=vector.c[(b_central-1) -sig ][0]
                                cont+=1
                        else:
                                sig= cont//2
                                ways.c[k+sig][rendija]=vector.c[(b_central-1) +sig ][0]
                                cont+=1
                k+=b_central
                rendija+=1
        #tercera parte de llenado       
        for i in range(n_blancos):
                ways.c[len(ways.c)-1-i][len(ways.c)-1-i]=complejo(1,0)
                
        return ways
def comprobar_Parametros_Multi(n_blancosPorRendija,b_central,n_rendijas,n_blancos):
        try:
                if(not(n_blancosPorRendija+( b_central*(n_rendijas-1) )== n_blancos)):
                        print(n_blancosPorRendija+( b_central*(n_rendijas-1) ), n_blancos)
                        raise ValueError("El numero de blancos por rendija no es compatible con el numero de blancos , por favor intente nuevamente")
        except ValueError:
                print("Failed :")
                raise
def matriz_multirendija(n_rendijas,n_blancos,vector_prob):
        # si me ingresa un numero general de probabilidades  en vez de un vector , se convierte a vector
        if (isinstance(vector_prob,float)):
                n_blancosPorRendija=int(vector_prob**(-1))
                vector_prob=    matriz.iniciar(int(vector_prob**(-1)),1)
                for  i in range(n_blancosPorRendija):
                        vector_prob.c[i][0]=complejo(1/n_blancosPorRendija,0)

        n_blancosPorRendija = len(vector_prob.c)
        tam_matriz=n_rendijas+n_blancos+1
        b_central=int((n_blancosPorRendija//2)+1)

        comprobar_Parametros_Multi(n_blancosPorRendija,b_central,n_rendijas,n_blancos)
        
        return make_matrix(tam_matriz,n_blancosPorRendija ,n_rendijas,n_blancos,b_central,vector_prob)

def experimento_multirendija_cuantico(n_rendijas,n_blancos,vector_prob):
    
        m=matriz_multirendija(n_rendijas,n_blancos,vector_prob)
        m= m.potencia(2)
        #print(m)
        for i in range(len(m.c)):
                for j in range(len(m.c[0])):
                        m.c[i][j]=complejo(m.c[i][j].modulo()*m.c[i][j].modulo(),0)              
        v= matriz.iniciar(len(m.c),1)
        v.c[0][0]=complejo(1,0)
        stat= m.alcanceSobre(v)
        #matriz.graficar(stat)
        return m,stat
        
        
def experimento_multirendija_probabilistico(n_rendijas,n_blancos,vector_prob):
        m=matriz_multirendija(n_rendijas,n_blancos,vector_prob)
        v= matriz.iniciar(len(m.c),1)
        v.c[0][0]=complejo(1,0)
        stat= m.state(v,2)
        #matriz.graficar(stat)
        return m,stat
        
def graficar(stat):
        axis_x= []
        axis_y=[]
        for i in range( len(stat.c)):
                axis_x.append(i)
        for j in range( len(stat.c)):
                axis_y.append(stat.c[j][0].real)
        
        fig = plt.figure(u'Vectores de resultado') # Figure
        ax = fig.add_subplot(111) # Axes
        datos = axis_y
        xx = range(len(datos))
        nombres=axis_x
        ax.bar(xx, datos, width=0.8, align='center')
        ax.set_xticks(xx)
        ax.set_xticklabels(nombres)
        plt.show()
