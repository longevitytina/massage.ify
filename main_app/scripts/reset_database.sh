#!/bin/bash
dropdb massageify
createdb massageify
python ../manage.py makemigrations
python ../manage.py migrate
python ../manage.py loaddata techniques
echo "from django.contrib.auth.models import User; User.objects.create_superuser('tina', 'tina@email.com', '1234 ')" | python ../manage.py shell
