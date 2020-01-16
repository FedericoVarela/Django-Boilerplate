@ECHO OFF
::call path/to/env

python manage.py makemigrations

python manage.py migrate