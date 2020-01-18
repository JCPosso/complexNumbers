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
            #Retorna division de dos numeros complejos a 2  decimales
            x=(self.real*b.real+self.img*b.img)
            y=(b.real*self.img-self.real*b.img)
            divisor=( b.real**2)+ (b.img**2) 
            if(divisor==0):
                return ("Divisor is zero!!")
            else :
                return (round(x/divisor,2),round(y/divisor,2))
              
        def modulo(self):
            #Retorna el modulo del numero complejo
            mod= math.sqrt(self.real**2+self.img**2)

            return (round(mod,2))

        def conjugado(self):
            #Retorna el conjugado del numero complejo
            return (self.real*-1,self.img*-1)

        def aPolar(self):
           #Retorna Coordenada polar del numero complejo
            fhi=round(math.sqrt(self.real**2+self.img**2),2)
            ang=round(math.atan(self.img/self.real),2)
            if( self.real==0 ):
                return ("NOT possible to convert!")
            else :
                return (fhi,ang)
              
        def fase(self):
            #Retorna la fase del numero complejo
            return round(math.atan2(self.img,self.real),2)
