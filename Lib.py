import math;
"""Librería computación Cuántica: Números complejos
   librería para hacer operaciones entre números complejos.
   @author (Juan Camilo Posso G.) 
   @version (1.0 or 16/01/2020)
"""
class complejo:
        def __init__(self,r,i):
            self.real= r
            self.img= i
        def suma(self,b):
            #suma de dos numeros complejos
            real = self.real + b.real
            img  = self.img + b.img
            return (real,img)
       
        def resta(self,b):
            #suma de dos numeros complejos
            real = self.real - b.real
            img  = self.img - b.img
            return (real,img)

        def multiplica(self,b):
            #Retorna multiplicacion de dos numeros complejos
            real=self.real*b.real - self.img*b.img
            img= self.real*b.img + b.real*self.img
            return (real,img)
       
        def divide(self,b):
            #Retorna division de dos numeros complejos
            x=(self.real*b.real+self.img*b.img)
            y=(b.real*self.img-self.real*b.img)
            divisor=( b.real**2)+ (b.img**2) 
            if(divisor==0):
                return ("Divisor is zero!!")
            else :
                return (x/divisor,y/divisor)
              
        def modulo(self):
            #Retorna el modulo del numero complejo
            mod= math.sqrt(self.real**2+self.img**2)
            return mod

        def conjugado(self):
            #Retorna el conjugado del numero complejo
            return (self.real*-1,self.img*-1)

        def aPolar(self):
           #Retorna Coordenada polar del numero complejo
            fhi=math.sqrt(self.real**2+self.img**2)
            ang=math.atan(self.img/self.real)
            if( self.real==0 ):
                return ("NOT possible to convert!")
            else :
                return (fhi,ang)
              
        def fase(a):
            #Retorna la fase del numero complejo
            return math.atan2(self.img,self.real)


 




