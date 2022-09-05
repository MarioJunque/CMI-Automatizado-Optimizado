# CMI-Automatizado-Optimizado
Este repositorio está dedicado al desarrollo del proyecto para crear una herramienta software que optimice y automatice la representación de CMI (Cuadros de Mando Integrales)

INSTALACIÓN 

Para poder usar la aplicación el usuario necesitará primero instalar Python, se recomienda utilizar la versión 3.8 o superior.

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

Tutorial Numpy:[Manual de instalación de Numpy](https://numpy.org/install/).

Tutorial Pandas:[Manual de instalación de Pandas](https://pandas.pydata.org/docs/getting_started/install.html).

Tutorial Django:[Manual de instalación de Django](https://docs.djangoproject.com/en/4.1/topics/install/).

Tutorial scikit-learn:[Manual de instalación de scikit-learn](https://scikit-learn.org/stable/install.html).

Tutorial setuptools:[Manual de instalación de setuptools](https://pypi.org/project/setuptools/).


Una vez realizada la instalación de estos paquetes el usuario ya puede usar en su sistema la aplicación.

CONDICIONES DE LA FUENTE DE DATOS

El usuario deberá de suministrar un archivo CSV separados por comas los valores tendría el siguiente formato de campos:

Row ID,Order ID,Order Date,Ship Date,Ship Mode,Customer ID,Customer Name,Segment,Country,City,State,Postal Code,Region,Product ID,Category,Sub-Category,Product Name,Sales,Quantity,Discount,Profit

Un ejemplo de una columna de valores que tendría cada campo sería el siguiente:

49,CA-2016-169194,20-06-16,25-06-16,Standard Class,LH-16900,Lena Hernandez,Consumer,United States,Dover,Delaware,19901,East,TEC-PH-10003988,Technology,Phones,"LF Elite 3D Dazzle Designer Hard Case Cover, Lf Stylus Pen and Wiper For Apple Iphone 5c Mini Lite",21.8,2,0,6.104

