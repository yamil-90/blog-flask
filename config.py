import os
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


MYSQL_DATABASE_HOST=environ.get('MYSQL_DATABASE_HOST')
MYSQL_DATABASE_USER=environ.get('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD=environ.get('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE_Db=environ.get('MYSQL_DATABASE_Db')
CARPETA = os.path.join('images')
SECRET_KEY = environ.get('SECRET_KEY')