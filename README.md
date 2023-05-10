Para esta prueba se uso django rest framework implementando 3 aplicaciones para cada uno de los modelos diseñados en el diagrama e-r 
Tambien se uso psycopg2 para la implementacion de postgresql 
Y de orm se uso qureysets y modelos para realizar las consultas por medio de las apiview de django y los modelos para generar la estructura de datos en la base de datos.

Script para crear la bd en postgresql: 
-- Database: prueba_tecnica

-- DROP DATABASE IF EXISTS prueba_tecnica;

CREATE DATABASE prueba_tecnica
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

Pasos para configurar postgresql en el proyecto
pip install psycopg2  

Luego de instalarlo cofiguramos la conexion en el archivo local.py en la carpeta settings alojada en la carpeta sistema_transporte

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prueba_tecnica',
        'USER': 'postgres',
        'PASSWORD': 'wilson2001',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

esta es la parte de codigo que se cambia, toca poner el usuario de postgresql que se tiene localmente por lo general es postgres o root , la contraseña de ese usuario y ya el resto se deja normal

Por ultimo creamos las migraciones con el comando
python3 manage.py makemigrations

Y luego realizamos las migraciones en la base de datos
python3 manage.py migrate

Por ultimo se levanta el servidor con el comando
python3 manage.py runserver


Adicionalmente si se quiere interactuar con el administrador de django toca antes de levantar el servidor, correr este comando: 
python3 manage.py createsuperuser

se ingresan los datos que se solicita y se levanta el servidor para acceder al djando admin

Por ultimo, las versiones de todas las herramientas utilizadas en el proyecto se encuentran en el archivo requirements.txt

// pip freeze del entorno (env)
python-decouple==3.8 🌟
django-cors-headers==3.14.0 🌟
asgiref==3.6.0
Django==4.2
djangorestframework==3.14.0
psycopg2==2.9.6
pytz==2023.3
sqlparse==0.4.3
tzdata==2023.3

Se hizo uso de python-decouple para separar la configuración sensible de la aplicación, como claves secretas, credenciales de base de datos y otros parámetros específicos del entorno. Esto permite una mejor gestión y seguridad en la configuración.

Se hizo uso de django-cors-headers para habilitar la funcionalidad de Cross-Origin Resource Sharing (CORS) en el proyecto Django. Esto permite que el proyecto acepte y restringa solicitudes HTTP de diferentes orígenes.
