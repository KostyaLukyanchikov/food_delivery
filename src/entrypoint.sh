#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py makemigrations menu shopping_cart orders users
python manage.py migrate
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
python manage.py runserver 0:8000

exec "$@"