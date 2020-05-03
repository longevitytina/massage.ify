#!/bin/bash
dropdb massageify
createdb massageify
python ../manage.py makemigrations
python ../manage.py migrate
python ../manage.py loaddata techniques