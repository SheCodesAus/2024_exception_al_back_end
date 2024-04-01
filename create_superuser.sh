#!/bin/bash

echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@email.com', 'Password1!')" | python3 manage.py shell
