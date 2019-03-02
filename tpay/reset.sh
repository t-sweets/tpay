find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -name "db.sqlite3" -delete

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser