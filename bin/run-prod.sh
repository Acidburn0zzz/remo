#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py compress --engine jinja2 --extension=.jinja
gunicorn remo.wsgi:application -b 0.0.0.0:${PORT:-8000} --log-file -
