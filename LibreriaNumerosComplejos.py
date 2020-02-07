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
        def __eq__(self, other):
            """Override"""
            if isinstance(other, complejo):
                return( self.real == other.real and self.img == other.img)
            return False

        
        def suma(self,b):
            #suma de dos numeros complejos
            real = self.real + b.real
            img  = self.img + b.img
            return complejo(real,img)
       
        def resta(self,b):
            #suma de dos numeros complejos
            real = self.real - b.real
            img  = self.img - b.img
            return complejo(real,img)

        def multiplica(self,b):
            #Retorna multiplicacion de dos numeros complejos
            real=self.real*b.real - self.img*b.img
            img= self.real*b.img + b.real*self.img
            return complejo(real,img)
       
        def divide(self,b):
            #Retorna division de dos numeros complejos a 2  decimales
            x=(self.real*b.real+self.img*b.img)
            y=(b.real*self.img-self.real*b.img)
            divisor=( b.real**2)+ (b.img**2) 
            if(divisor==0):
                return ("Divisor is zero!!")
            else :
                return complejo(round(x/divisor,2),round(y/divisor,2))
              
        def modulo(self):
            #Retorna el modulo del numero complejo
            mod= math.sqrt(self.real**2+self.img**2)

            return (round(mod,2))

        def conjugado(self):
            #Retorna el conjugado del numero complejo
            return complejo(self.real,self.img*-1)

        def aPolar(self):
           #Retorna Coordenada polar del numero complejo
            if( self.real==0 ):
                return ("NOT possible to convert!")
            else :
                fhi=round(math.sqrt(self.real**2+self.img**2),2)
                ang=round(math.atan2(self.img,self.real),2)
                return complejo(fhi,ang)
              
        def fase(self):
            #Retorna la fase del numero complejo
                
            if(self.real==0):return "indefinido!!"
            res= round(math.atan2(self.img,self.real),2)
            return res

        def __str__(self):
                s1=str(self.real)
                if(self.img!=1 and self.img!=-1 ):
                        s2=str(self.img)+"i"
                else:
                        if (self.img==-1):s2="-i"
                        else :s2="i"

                if(self.real==0):
                        if (self.img==0):return '0'
                        else            :return s2
                else:
                        
                        if (self.img>0):return s1+"+"+s2
                        if (self.img<0):return s1+s2
                return s1
