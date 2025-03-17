#!/bin/bash

mkdir -p /code/logs
test -f /code/logs/django_danger.log || touch /code/logs/django_danger.log
test -f /code/logs/django_debug.log || touch /code/logs/django_debug.log
test -f /code/logs/django_info.log || touch /code/logs/django_info.log
chown nobody:nogroup /code/logs/*.log
chmod 666 /code/logs/*.log

while [ "1"=="1" ]
do
    python3 manage.py runserver 0.0.0.0:8000
    sleep 1
done
