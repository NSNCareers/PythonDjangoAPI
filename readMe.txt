To install virtualenv run:
pip3 install virtualenv

cd to your project:
virtualenv venv

Activate environment:
source venv/bin/activate

select path to pyhton enterpreter:
"venv/bin/python"

close virtual env:
deactivate

return to virtual env:
workon PythonDjangoAPI

Create requiremets file 
pip3 freeze > requirements.txt

run django server
python manage.py runserver 0.0.0.0:8080


Install dependencies
pip3 install -r requirements.txt


Create a Migration
python manage.py makemigrations

Migrate
python manage.py migrate