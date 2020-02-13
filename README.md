Este proyecto esta realizado con **React** + **GrapQL** + **Django**.
A continuacion se presenta un manual para configurar tu entorno de desarrollo desde cero.
>_**Para gestionar los paquetes de Python, en este proyecto usamos [Anaconda](https://www.anaconda.com/).**_

# 1. Configuracion directorio `Django`
## 1.1 Entorno virtual
Lo primero que haremos es crear un entorno virtual en **`Anaconda`**, para asi poder instalar nuestros paquetes de forma local, y no global en nuestra PC.
Usamos el siguiente comando:
``` sh
conda create --name djangoenv python = 3.8
```
> La palabra _`djangoenv`_ es el nombre que tendrá nuestro entorno, sientete libre de usar el nombre que quieras.

Para empezar a trabajar sobre el nuevo entorno, tenemos que activarlo, lo hacemos con el siguiente comando:

``` bash
conda activate djangoenv
```
Y cuando quiera desactivarlo:
``` bash
conda deactivate
```
## 1.2 Instalación de **`Django`**
Dentro de nuestro nuevo entorno virtual, instalamos _`django`_ usando el siguiente comando:
``` sh
conda install -c conda-forge django
```
## 1.3 Directorio de trabajo
A diferencia de otros frameworks como Laravel, el directorio de nuestro proyecto Django no necesita estár en la carpeta `www/` de nuestro servidor **Apache**, puede crear un proyecto **Django** en el directorio que quiera, con el comando `cd` podemos navegar al directorio deseado:
``` bash
cd Documentos/www/
```
Creamos y accedemos a la carpeta  que va a contener nuestro proyecto:
``` bash
mkdir projectRGD
cd projectRGD/
```
En este punto ya tenemos la carpeta que almacenara nuestro proyecto entero y accedimos a ella.

## 1.4 Comando `git init`

En la carpeta actual escribiremos el siguiente comando que nos permitira hacer un control de versiones de nuestro proyecto:
``` sh
git init
```
Luego manualmente creamos los archivos **`.gitignore`** y **`readme.md`**, nuestro directorio debe verse asi:
``` diff
projectRGD/
+	/* .gitignore
+	/* readme.md
```
## 1.5 Creacion del proyecto django

Con el siguiente comando crearemos un proyecto django:
``` bash
django-admin startproject project_start
```
Esto crea una nueva carpeta _`project_start`_ con varios subdirectorios y archivos:
``` diff
projectRGD/
+	project_start/
+		project_start/
+			/* __init__.py
+			/* asgi.py
+			/* settings.py
+			/* urls.py
+			/* wsgi.py
+		/* manage.py
	/* .gitignore
	/* readme.md
```
 a la cual accedemos usando:
``` bash
cd project_start
```
> Recuerda que `project_start` es solo el nombre del proyecto, sientete libre de elegir el que quieras.

Ahora tenemos el siguiente contenido en el directorio actual:
``` diff
project_start/
	project_start/
		/* __init__.py
		/* asgi.py
		/* settings.py
		/* urls.py
		/* wsgi.py
	/* manage.py
```
> En este punto ya podemos probar el proyecto con un servidor de desarrollo proporcionado por django, para eso usamos en siguiente comando: **`python manage.py runserver`**.
## 1.6 Creacion de una aplicación
> ### Aplicacion vs Proyecto
>> Un proyecto puede contener una o mas aplicaciones, las aplicaciones son pequeñas partes del software que esta diseñada para un uso especifico.

Crearemos una aplicacion que contendra nuestros directorios de **`React`**, la llamaremos _`frontend`_, usaremos el siguiente comando:
``` bash
python manage.py startapp frontend
```
Este comando creo los siguientes directorios y archivos:
``` diff
project_start/
+	frontend/
+		migrations/
+			/* __init__.py
+		/* __init__.py
+		/* admin.py
+		/* apps.py
+		/* models.py
+		/* test.py
+		/* views.py
	project_start/
		/* __init__.py
		/* asgi.py
		/* settings.py
		/* urls.py
		/* wsgi.py
	/* manage.py
```
# 2. Configuracion directorio `React`
