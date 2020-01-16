@ECHO OFF
::call path/to/env

::Tests all apps at once. 
python manage.py test 

:: For individual apps:
:: python manage.py test appname