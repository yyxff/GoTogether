#!/bin/bash

mkdir -p /code/logs
test -f /code/logs/django_danger.log || touch /code/logs/django_danger.log
test -f /code/logs/django_debug.log || touch /code/logs/django_debug.log
test -f /code/logs/django_info.log || touch /code/logs/django_info.log
chown nobody:nogroup /code/logs/*.log
chmod 666 /code/logs/*.log


python3 manage.py makemigrations
python3 manage.py migrate
res="$?"
while [ "$res" != "0" ]
do
    sleep 3;
    python3 manage.py migrate
    res="$?"
done

