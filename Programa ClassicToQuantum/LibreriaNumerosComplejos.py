import math;
class complejo:
        '''
        Libreria de Numeros complejos de argumentos r,i en donde r e i son las componentes cartesianes
        real e imaginaria , respectivamente.Todos los atributos se daran tanto en pares de  complejos
        o de forma unaria.
        '''
        def __init__(self,r,i):
                self.real= r
                self.img= i
        def __eq__(self, other):
                """Override"""
                if isinstance(other, complejo):
                        return( round(self.real,2) == round(other.real,2) and round(self.img,2) == round(other.img,2))
                return False
        def suma(self,b):
                '''
                Retorna la suma de dos complejos.

                Excepciones:
                si alguno de los dos numeros no es un complejo
                '''
                self.compare(b)
                real = self.real + b.real
                img  = self.img + b.img
                return complejo(real,img)
        def resta(self,b):
                '''
                Retorna la resta de dos complejos.

                Excepciones:
                si alguno de los dos numeros no es un complejo
                '''
                self.compare(b)
                real = self.real - b.real
                img  = self.img - b.img
                return complejo(real,img)
        def multiplica(self,b):
                '''
                Retorna la multiplicación de dos complejos.

                Excepciones:
                Si alguno de los dos numeros no es un complejo
                '''
                self.compare(b)
                real=self.real*b.real - self.img*b.img
                img= self.real*b.img + b.real*self.img
                return complejo(real,img)
        def divide(self,b):
                '''
                Retorna la división de dos complejos.
                Parte real e imaginaria redondeados a dos decimales.

                Excepciones:
                si alguno de los dos numeros no es un complejo
                Si el divisor es cero
                '''
                self.compare(b)
                try:
                        x=(self.real*b.real+self.img*b.img)
                        y=(b.real*self.img-self.real*b.img)
                        divisor=( b.real**2)+ (b.img**2)
                        return complejo(x/divisor,y/divisor)
                except ZeroDivisionError as m:
                        raise Exception("Division por 0!!!")
        def modulo(self):
                '''
                Retorna la módulo del complejo.
                Redondeado a dos decimales.
                '''
                mod= math.sqrt(self.real**2+self.img**2)
                return  mod
        def modulo_cuadrado(self):
                return self.real**2+self.img**2
        def conjugado(self):
                '''
                Retorna conjugado del complejo.
                '''
                return complejo(self.real,self.img*-1)
        def aPolar(self):
                '''
                Retorna el numero en coordenadas polares.
                
                Excepciones:
                Si la Parte real es cero
                '''
                try:
                        fhi=round(math.sqrt(self.real**2+self.img**2),2)
                        ang=round(math.atan2(self.img,self.real),2)
                        return complejo(fhi,ang)
                except ZeroDivisionError as m:
                        raise Exception("Parte Real es Cero!!!")
        def fase(self):
                '''
                Retorna la Fase del número.
                
                Excepciones:
                Si la Parte real es cero
                '''
                try:
                        res= round(math.atan2(self.img,self.real),2)
                        return res
                except ZeroDivisionError as m:
                        raise Exception("Parte Real es Cero!!!")
        def compare(self,r):
                if (not (isinstance(self,complejo) and isinstance(r,complejo)) ) :
                        raise Exception("ERROR:Favor Ingresar un formato válido")

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
