## Simulacion Cuantica 
* SimulacionCuantica.py es una Libreria que permite diseñar y probar distintos experimentos al estilo doble rendija y multirendija tanto probabilistico como cuántico , en donde se permiten realizar las siguientes operaciones:
>- Experimento Multirendijas cuantico.
>- Experimento Multirendijas probabilistico.
>- Graficar vectores (Matplotlib).

## Comenzando 🚀
* Clone éste repositorio en su máquina local usando [ComplexNumbers](https://github.com/JCPosso/complexNumbers.git)- Repositorio

Para un buen Uso de la Libreria es Necesario  que al hacer uso de las distintas funciones de 'SimulacionCuantica.py' es necesario conocer los distintos parámetros de ambas funciones las cuales son:

* n_rendijas = Numero de rendijaas del sistema
* n_blancos = Numero de blancos del sistema
* vector_prob = Un vector de probabilidad de clase matriz , con las probabilidades de ir de cada rendija a cada uno de sus objetivos , o también se puede ingresar el numero de probabilidad asociado en el caso de los experimentos multirendija probailisticos  .

El nommbre de cada una de las funciones con susrespectivos prametros son :
```
>-experimento_multirendija_cuantico(n_rendijas,n_blancos,vector_prob) 
 --->retorna : Matriz final con sus respectivas interferencias  y vector final caracteristico asociado al sistema
 
>-experimento_multirendija_probabilistico(n_rendijas,n_blancos,vector_prob)
 --->retorna : Matriz construida  a partir de los datos ingresados y vector final caracteristico asociado al sistema
```
### Pre-requisitos 📋
* Libreria MatPlotLib
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
Para ejecutar los test debe descargar el archivo 'test_simulClassicToCuant.py' en donde se encuentra distintos experimentos con sus respectivas gráficas asociadas .
Ejecute las prueblas 'test_simulClassicToCuant.py' .
Pruebas test_clasicTocuant.py Para revisar funcionamiento de las funciones para n-rendijas de forma probabilistica o cuantica.

### Pruebas end-to-end 🔩
Se realizaron para ver su funcionamiento en sistemaas multirendija para dos y tres rendijas  probabilisticas como cuanticas.
A continuacion ,un Ejemplo de prueba para ver fenomeno interferencia para 3 rendijas cuantico y comprobar que la matriz resultante y el estado asociado al sistema sea el esperado :
```
        def test02_Multirendija_Cuantico_TresRendijas(self):
                v= matriz([ [[-math.sqrt(10)/10,math.sqrt(10)/10]],[[-math.sqrt(10)/10,math.sqrt(10)/10]],[[-math.sqrt(10)/10,-math.sqrt(10)/10]],[[math.sqrt(10)/10,-math.sqrt(10)/10]],[[math.sqrt(10)/10,-math.sqrt(10)/10]] ])
                matrizCaminos, estado     =    experimento_multirendija_cuantico(3,11,v)
                
 ### Aquí comprobamos que los resultados sean los esperados:            
 
                self.assertTrue(matrizCaminos ==matriz([ [  [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[1/5,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[1/5,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0] ],
                                                          [ [0,0],[0,0],[1/5,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0],[0,0] ],
                                                          [ [1/15,0],[0,0],[0,0],[1/5,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[1,0] ], ] ))
               
                self.assertTrue(estado == matriz([ [[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]],[[ 0,0 ]]
                                                ,[[1/15,0]],[[ 1/15,0]],[[ 1/15,0]],
                                                [[ 0,0 ]],[[ 0,0 ]],[[1/15,0]],[[ 0,0 ]],[[ 0,0 ]],
                                                [[ 1/15,0]],[[ 1/15,0]],[[ 1/15,0]] ]))
                graficar(estado)
```
Como al final hicimos uso de la funcion 'graficar(estado)' ,obtenemos el siguiente diagrama de barras correspondiente al estado final del sistema el cual permite ver de manera clara su comportamiento final Y el distintivo patron de interferencia asociado:
![](src/10.PNG)

# Simulacion Práctica

## Historia
El experimento de Young, realizado en 1801 por Thomas Young , con el fin de comprobar la naturaleza Ondulatoria de la luz .
### Simulacion doble rendija libreria
Con la libreria se pretendió revisar como surgia el patron de interferencia para luego ser comparado con los resultados experimentales obtenidos.
A continuacion  vemos como se determina el experimento  para doble rendija en la libreria y se toma el siguiente experimento
![](src/6.PNG)

* Se logró observar como se generaba el efecto . Primero , como se vio anteriormente se procedio a ingresar un vector  de estado inicial.

![](src/7.PNG)
* Luego ,  se procedio a ingresar el numero de rendijas del sistema , los blancos y el vector de probabilidades de cada rendija a cada blanco .
![](src/8.PNG)
* Para hallar la matriz de probabilidades , se  halló el modulo al cuadrado de cada  uno de los numeros lo cual nos genera la siguiente matriz:
![](src/9.PNG)
* Y por ultimo se ingreso el vector de estado en donde  el fotón se enuentra en la primra parte del sistema  de la siguiente forma 
Al terminar la simulacon se procedio a graficar el vector de estados resultantes: y el resultado fue el siguiente :

![](src/4.png)

## Experimento
### Materiales 
Para la realizacion del experimento se realizo con los siguientes materiales  :
>- Cartón paja.
>- Láser común.
>- Silicona Líquida y en barra.
>- Aluminio.
>- cinta aislante.
>- Bisturí.
>- Regla.
## Procedimiento 🚀
*  Se hicieron varios cortes al carton paja para crear tanto  la pared donde se es proyectada la interferencia  para crear luego , las distintas rendijas por donde pasaba la luz estas a su vez se mueven mientras se deslizan a una distancia prudente del laser como de la pared.
*Para crear la rendija se hicieron cortes en una base rectangular en el cual se hicieron varios cortes con cuadrados de 3.5 cm separados a una distancia equidistante ,  luego con el bisturí se hicieron cortes sobre unos cuadrados de aluminio*1 , 2 y 3 cortes en cuada cuadro)  de una tamano mas grande que los cuadros hechos sobre la base rectangular de carton paja . Por ultimo , se pegaron con cinta aislante .
* Se unieron todos los componentes  a  un cuarto de cartón paja con silicona y se dio paso a la realizacion del experimento.

### Desarrollo 
Para realizar el experimento se procedio a colocar el laser sobre su base , siendo presionado con cinta aislante , luego se procedio a poner la base de 3 rectangular de rendijas sobre un soporte por el cual se va deslizando para que la luz del laser pasara por cada una de las rendijas , como se muestra a continuacion.

![](src/2.jpeg)

### Resultados ⚙️

A continuacion se muestran las Imagenes  del  fenomeno de interferencia ocasionado por cada una de las rendijas elaboradas.

[![VideoLink](src/3.jpeg)](https://www.youtube.com/watch?v=ww_fMEEHPKs)


### Conclusiones📋
En conclusion , se pudo observar y analizar como  la luz del laser tuvo dos comportamientos antes y despues de pasar por las rendijas , antes la luz se fragmentaba en cada una de las posibles rendijas por donde se podia pasar y luego de pasar por estas   se produce un fenomeno de interferencia haciendo que algunos lugares del patron se vean oscuros y otros mas claros , tal cual como sucede con la interferencia ondulatoria. Cuando mas aumentabamos el nivel de rendijas el patron se hacia mas alargado  tal como se mostrababa en las imagenes
según lo observado se ve que el resultado se asemeja más al comportamiento de ondas con el patrón de interferencia, pero esto en la época del experimento desconsternaba a los científicos el hecho de que al poner detectores después de la rendija para saber por dónde pasaba la luz el patrón del experimento era equivalente al de las partículas, lo que nos da entender que cuando el experimento está siendo monitoreado nos da como resultado el de las partículas y cuando no el resultado es el de patrón de interferencia de las ondas, como se muestra a continuación:
![](src/1.jpeg)

## Autor(es) ✒️

* **Juan Camilo PossoG.** - *Initial work* - [JCPosso](https://github.com/JCPosso)

* Personas que han contribuido al proyecto : [contribuyentes](https://github.com/JCPosso/complexNumbers/contributors)

## Referencias
Inspirando en:

*Michael A. Nielsen, Isaac L. Chuang. Quantum Computation and Quantum Information (10th Anniversary edition). Cambridge University Press. 2016
