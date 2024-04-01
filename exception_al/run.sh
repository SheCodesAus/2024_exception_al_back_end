#!/usr/bin/env bash
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'Password1!')" | python manage.py shell
gunicorn --bind :8000 --workers 1 exception_al.wsgi
