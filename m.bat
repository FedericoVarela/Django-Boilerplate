@ECHO OFF
call conda activate

python manage.py makemigrations

python manage.py migrate