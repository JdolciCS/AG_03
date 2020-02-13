Este proyecto esta realizado con **React** + **GrapQL** + **Django**.

A continuacion se presenta un manual para configurar tu entorno de desarrollo desde cero.

>_**Para gestionar los paquetes de Python, en este proyecto usamos [Anaconda](https://www.anaconda.com/).**_

## Entorno virtual
> Lo primero que haremos es crear un entorno virtual en anaconda, para poder instalar nuestros paquetes de forma local, y no global en nuestra PC. Usamos el siguiente comando:

``` sh
conda create --name djangoenv python = 3.8
```
> La palabra `djangoenv` es el nombre que tendrá nuestro entorno, sientete libre de usar el nombre que quieras.

> Para empezar a trabajar sobre el nuevo entorno, tenemos que activarlo, lo hacemos con el siguiente comando:

``` sh
conda activate djangoenv
```
> Y cuando quiara desactivarlo:

``` sh
conda deactivate
```

## Instalacion de djando

> Dentro de nuestro nuevo entorno virtual, instalaremos django usando el siguiente comando:

``` sh
conda install -c conda-forge django
```

## Directorio de trabajo
> A diferencia de otros frameworks como Laravel, el directorio de nuestro proyecto Django no necesita estár en la carpeta `www/` de nuestro servidor apache, puede crear un proyecto Django en el directorio que quiera, con el comando `cd` navegaremos al directorio deseado:

``` sh
cd Documentos/www/
```
> Creamos y accedemos a la carpeta  que va a contener nuestro proyecto:

``` sh
mkdir projectRGD
cd projectRGD/
```

> En este punto ya tenemos la carpeta que almacenara nuestro proyecto entero y accedimos a ella.

## Comando `git init`

> Escribiremos el siguiente comando que nos permitira hacer un control de versiones de nuestro proyecto:

``` sh
git init
```
> luego manualmente creamos los archivos **`.gitignore`** y **`readme.md`**, nuestro directorio debe verse asi:

``` diff
projectRGD/
+	/* .gitignore
+	/* readme.md
```

## Creacion del proyecto django

> Con el siguiente comando crearemos un proyecto django:

``` sh
django-admin startproject project_start
```

> Esto crea una nueva carpeta `project_start` y varios subdirecrotios con archivos:

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

 > a la cual accedemos usando:

``` sh
cd project_start
```

> Recuerda que `project_start` es solo el nombre del proyecto, sientete libre de elegir el que quieras.
> Ahora tenemos el siguiente contenido en el directorio actual:

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

> En este punto ya podemos probar el proyecto con un servidor de desarrollo proporcionado por django, para eso usamos en siguiente comando:

``` sh
python manage.py runserver
```

## Creacion de una aplicacion

> ### Aplicacion vs Proyecto
>> Un proyecto puede contener una o mas aplicaciones, las aplicaciones son pequeñas partes del software que esta diseñada para un uso especifico.

>  Crearemos una aplicacion que contendra nuestros directorios de **`React`**, la llamaremos `frontend` y usaremos el siguiente comando:

``` sh
python manage.py startapp frontend
```

> Este comando creo los siguientes directorios y archivos:

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
