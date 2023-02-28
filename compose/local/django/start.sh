#!/bin/sh

set -o errexit
set -o nounset

#python manage.py makemigrations
#python manage.py migrate
#python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin@gmail.com', 'admin')"

python manage.py runserver 0.0.0.0:8000
