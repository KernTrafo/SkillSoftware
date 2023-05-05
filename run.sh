#!/bin/sh
flask db init
flask db migrate
flask db upgrade
exec gunicorn -b 0.0.0.0:8000 -w 2 main:app
