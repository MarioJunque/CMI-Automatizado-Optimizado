# CMI-Automatizado-Optimizado
Este repositorio está dedicado al desarrollo del proyecto para crear una herramienta software que optimice y automatice la representación de CMI (Cuadros de Mando Integrales)

INSTALACIÓN 

Esta aplicación solo funciona en sistemas Windows, recomendable que sean con versiones **Windows 10 o superior**.

El usuario deberá de instalar la aplicación Power BI desktop.

Puede descargarla en Microsoft Store o en el siguiente enlace: 
[Enlace de descarga de Power BI](https://powerbi.microsoft.com/es-es/downloads/).

Para poder usar la aplicación el usuario necesitará tambien instalar Python, se recomienda utilizar la versión 3.8 o superior.

Puede descargarlo en el siguiente enlace: 
[Enlace de descarga de Python](https://www.python.org/downloads/).

Una vez realizada la instalación podrá usar pip, el gestor de paquete de Python. Deberá abrir la línea de comando y escribir los siguientes comandos:

```
pip install numpy
```

```
pip install pandas
```

```
py -m pip install Django
```

```
pip install -U scikit-learn
```

```
pip install setuptools
```

Las versiones utilizadas para este proyecto han sido:

numpy 1.19.5

pandas 1.4.2

Django 4.0.5

sckit-learn 1.1.1

setuptools 62.3.2


Puede encontrar también sus correspondientes tutoriales de instalación en los siguientes enlaces:

Tutorial Numpy: [Manual de instalación de Numpy](https://numpy.org/install/).

Tutorial Pandas: [Manual de instalación de Pandas](https://pandas.pydata.org/docs/getting_started/install.html).

Tutorial Django: [Manual de instalación de Django](https://docs.djangoproject.com/en/4.1/topics/install/).

Tutorial scikit-learn: [Manual de instalación de scikit-learn](https://scikit-learn.org/stable/install.html).

Tutorial setuptools: [Manual de instalación de setuptools](https://pypi.org/project/setuptools/).


Una vez realizada la instalación de estos paquetes el usuario ya puede usar en su sistema la aplicación.

Para descargar en su sistema el repositorio use el siguiente comando en la linea de comandos:

```
git clone https://github.com/MarioJunque/CMI-Automatizado-Optimizado.git
```

Una vez descargado dentro de la carpeta con el nombre CMI-Automatizado-Optimizado donde dispondrá ya del proyecto.

A continuación debe de entrar a través de la linea de comando a la carpeta del proyecto usando el siguiente comando:

```
cd [Ruta a la carpeta del repositorio en su sistema]
```

Una vez dentro deberá de ejecutar el siguiente comando para instalar el proyecto:

```
python setup.py sdist --formats=zip
```
Se generará una carpeta con el nombre dist, para entrar en ella usar:

```
cd dist
```

y dentro de esta introducir el comando:

```
pip install paq_CMI-Automatizado-Optimizado-1.0.zip
```

De esta manera ya tendrá listo el proyecto para usar, deberá entrar a la linea de comandos a la carpeta BalancedScorecard:

```
cd [Ruta a la carpeta BalancedScorecard del repositorio]
```

Y ejecutar por último el comando que funciona exclusivamente en esta carpeta:

```
 python manage.py runserver
```

Este último comando deberá de usarlo siempre que quiera iniciar la aplicación

Para poder acceder a ella introduzca en el siguiente enlace en el navegador que desee: `127.0.0.1/home`

CONDICIONES DE LA FUENTE DE DATOS

El usuario deberá de suministrar al sistema un archivo CSV con nombre `superstore.csv` separados por comas los valores tendría el siguiente formato de campos:

Row ID,Order ID,Order Date,Ship Date,Ship Mode,Customer ID,Customer Name,Segment,Country,City,State,Postal Code,Region,Product ID,Category,Sub-Category,Product Name,Sales,Quantity,Discount,Profit

Puede encontrar un ejemplo del archivo en la carpeta `dataset` del repositorio con los distinto valores que pueden tomar los campos, tendrá el mismo nombre que el propuesto anteriormente, es decir, se llama `superstore.csv`.

