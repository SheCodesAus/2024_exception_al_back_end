#!/usr/bin/env bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --no-input
gunicorn --bind :8000 --workers 1 exception_al.wsgi