#!/bin/bash
gunicorn --bind 0.0.0.0:9000 kittygram_backend.wsgi
python manage.py migrate;
python manage.py collectstatic;
cp -r /app/collected_static/. /static/static/;
