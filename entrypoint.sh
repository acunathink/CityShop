
python manage.py makemigrations
python manage.py migrate --no-input

python manage.py collectstatic --no-input
cp -r /app/collected_static/. /backend/static

gunicorn config.wsgi --bind 0.0.0.0:8000
