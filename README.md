# Complex Numbers

ComplexNumbers es una libreria para el manejo de numeros complejos ,matrices complejas Útil para la realizacion de  simulaciones de circuitos cuánticos.

## Comenzando 🚀
* Clone éste repositorio en su máquina local usando [ComplexNumbers](https://github.com/JCPosso/complexNumbers.git)- Repositorio

### Pre-requisitos 📋

Python 3

```
How to install python 3?
Step 1: Download the Python 3 Installer. Open a browser window and navigate to the Download page for Windows at python.org. ...
Step 2: Run the Installer. Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file.

```
Git
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
siga instrucciones en https://git-scm.com/book/en/v2/Getting-Started-Installing-Git para ejecutar un entorno de desarrollo en git
## Ejecutando las pruebas ⚙️
Ejecute las prueblas test_numerosComplejos y test_vectoresyMatrices desde la IDLE .
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

## Versionado 📌
Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/JCPosso/complex Numers/tags).
Versiones actuales de la libreria :
* (https://github.com/JCPosso/complexNumbers/releases/tag/v1.0-Beta). 

## Autores ✒️

* **Juan Camilo PossoG.** - *Initial work* - [JCPosso](https://github.com/JCPosso)

* Personas que han contribuido al proyecto : [contribuyentes](https://github.com/JCPosso/complexNumbers/contributors)

## Licencia 📄

Este proyecto está bajo [LICENSE.txt](https://github.com/JCPosso/complexNumbers/blob/master/LICENCE.txt).

## Referencias
Inspirando en:
*Michael A. Nielsen, Isaac L. Chuang. Quantum Computation and Quantum Information (10th Anniversary edition). Cambridge University Press. 2016
