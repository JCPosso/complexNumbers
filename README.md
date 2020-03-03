# Complex Numbers

ComplexNumbers es una libreria para el manejo de numeros complejos ,matrices complejas Útil para la realizacion de  simulaciones de circuitos cuánticos.
## Resumen de las operaciones que se pueden hacer
Dentro de la libreria numerosComplejos.py  se pueden encontrar las distintas operaciones que se pueden realizar con numeros complejos tales como :
>- Sumar.
>- Restar.
>- Dividir.
>- Multiplicar.
>- Modulo.
>- Conjugado.
>- Pasar de coordenadas cartesianas a polares y viceviersa.
>- Fase.

Y por otro lado encontramos la libreria matrices.py la cual nos permite realizar las siguientes operaciones:

>- Adición de vectores complejos.
>- Inversa de vectores complejos.
>- Multiplicación escalar de vectores complejos.
>- Adición de matrices complejos.
>- Inversa de matrices complejos.
>- Multiplicación escalar de matrices complejas.
>- Matriz transpuesta.
>- Matriz conjugada.
>- Matriz adjunta.
>- Función para calcular la "acción" de una matriz sobre un vector.
>- Norma de matrices.
>- Distancia entrematrices.
>- Revisar si es unitaria.
>- Revisar si es Hermitian.
>- Producto tensor.
>- Experimento Multirendijas cuantico.
>- Experimento Multirendijas probabilistico.
>- Graficar vectores (Matplotlib).

## Comenzando 🚀
* Clone éste repositorio en su máquina local usando [ComplexNumbers](https://github.com/JCPosso/complexNumbers.git)- Repositorio

* Para hacer un buen uso de las funciones , cabe recordar que la entrada debe ser tipo matricial y para la creacion de numeros complejos en forma de tuplas  en donde se especifica la parte real e imaginaria como por ejemplo:
```
a= complejo(5,4)
b= complejo(5,0)
c= complejo(0,2)

```
y para la entrada de vectores y matrices , se realiza  como en el siguiente ejemplo :
```
#vector
V=matriz([ [[3,2]],[[1,9]],[[3,2]] ])
#matriz
A=matriz([ [[1,2],[3,2],[6,6]],[[9,9],[1,9],[0,0]],[[7,1],[4,5],[3,2]] ])
```

### Pre-requisitos 📋
* Sistemas operatrivos: mac , linux o windows.

* Editor de archivos .py

Python 3

```
How to install python 3?
Step 1: Download the Python 3 Installer. Open a browser window and navigate to the Download page for Windows at python.org. ...
Step 2: Run the Installer. Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file.

```
Git(opcional)
```
¿Como descargar git?

1.- Descargando Git
Para poder utilizar Git en nuestro equipo es importante realizar la descarga del software que contiene todos los comandos para poder gestionarlo.
Como primer paso nos dirigimos a la ruta https://git-scm.com/ para realizar la descarga,dando clic en la imagen del monitor que se encuentra a un costado, el cual contiene la descripción “Download NumeroVersion for windows”

2.- Ejecutando el instalador de git
Una vez descargado, daremos doble clic en el instalador y nos aparecerá la primera pantalla, donde daremos Next(Siguiente)

3.- Configurando ruta de instalación
Nos aparece otra ventana donde indicaremos la ruta donde deseamos guardar los archivos de configuración de Git, nosotros por lo pronto, la dejaremos así, pero puedes elegir la ruta que desees, daremos clic en Next(Siguiente)

4.- Configurando instalación de Git
En la siguiente pantalla nos muestra algunas configuraciones que podemos cambiar, como el editor de texto, si queremos colocar un icono en el escritorio y demás, por lo pronto lo dejaremos así, solo daremos clic en Next(Siguiente)

5.-Comprobando la instalación         
Para comprobar que Git se instaló correctamente solo vamos a Windows -> y escribimos Git, veremos que aparecerán los programas básicos para comenzar a trabajar con Git.
```
### Instalación 🔧
* Descargue los archivos de libreria
* Ponga las librerias en la carpeta en la cual se encuentra el proyecto
* Importe la libreria al archivo .py del proyecto
* Utilizce las funciones de libreria .

* *siga instrucciones en https://git-scm.com/book/en/v2/Getting-Started-Installing-Git para ejecutar un entorno de desarrollo en git

## Ejecutando las pruebas ⚙️
Para ejecutar los test debe descargar el archivo 'test_matrices.py' y 'test_numerosComplejos.py' en los cuales se encuentran las diferentes pruebas realizadas y los datos que deberia arrojar para distintos resultados.

Ejecute las prueblas test_numerosComplejos y test_matrices desde su editor .py .

Pruebas test_clasicTocuant.py Para revisar funcionamiento de las funciones para n-rendijas de forma probabilistica o cuantica.

### Pruebas end-to-end 🔩
Se realizaron pruebas para verificar , cómo se comportan las funciones para el tratamiento de los numeros complejos y si cumplen con las reglas basicas de aritmetica , asi como reglas algebraicas para la operacion adecuada de complejos , vectores y matrices .
```
Ejemplo de prueba para producto Tensor para verificar si se puede obtener un producto Tensor entrelazado:
  def test02_productoTensor(self):
        k=matriz([ [[1,0]],[[0,0]] ])
        b=matriz([ [[8,0]],[[0,0]],[[0,0]] ])
        c=matriz([ [[0,0]],[[6,0]] ])
        d=matriz([ [[0,0]],[[0,0]],[[3,0]] ])
        self.assertEqual(str((k.productoTensor(b)).suma(c.productoTensor(d))),'[ 8 ]\n[ 0 ]\n[ 0 ]\n[ 0 ]\n[ 0 ]\n[ 18 ]\n')
```
Estan pruebas tienen casos sacados del libro  , las distintas propiedades especificadas en éste y casos arbitrarios para corroborar su funcionamiento.

## Versionado 📌
Se usó [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [Tags del repositorio](https://github.com/JCPosso/complexNumbers/tags).

Versiones actuales de la libreria :
* (https://github.com/JCPosso/complexNumbers/releases/tag/v1.0-Beta). 

## Autores ✒️

* **Juan Camilo PossoG.** - *Initial work* - [JCPosso](https://github.com/JCPosso)

* Personas que han contribuido al proyecto : [contribuyentes](https://github.com/JCPosso/complexNumbers/contributors)

## Licencia 📄

Este proyecto está bajo licencia [LICENSE.txt](https://github.com/JCPosso/complexNumbers/blob/master/LICENCE.txt).

## Referencias
Inspirando en:

*Michael A. Nielsen, Isaac L. Chuang. Quantum Computation and Quantum Information (10th Anniversary edition). Cambridge University Press. 2016
