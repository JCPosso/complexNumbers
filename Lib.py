import math;

def suma(a,b):
    n1=a[0]+b[0]
    n2=a[1]+b[1]
    return (n1,n2)
def resta(a,b):
    n1=a[0]-b[0]
    n2=a[1]-b[1]
    return (n1,n2)
def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+b[0]*a[1])
def division(a,b):
    x1=(a[0]*b[0]+a[1]+b[1])
    x2=( b[0]**2)+ (b[1]**2) 
    y1=(b[0]*a[1]-a[0]*b[1])
    y2=((b[0]**2)+(b[1]**2))
  
    if( b[0]==0 or b[1]==0):
        return ("Divisor is zero!!")
    else :
        return (x1/x2,y1/y2)
def modulo(a):
    mod= math.sqrt(a[0]**2+a[1]**2)
    return mod

def conjugado(a):
    return (a[0],a[1]*(-1))

def cartesianToPolar(a):
    fhi=math.sqrt(a[0]**2+a[1]**2)
    ang=math.atan(a[1]/a[0])
    if( b[0]==0 or b[1]==0):
        return ("NOT possible to convert!")
    else :
        return (fhi,ang)
    
    //comiiit
  def fase(a):
    return math.atan2(a[1],a[0])


 




