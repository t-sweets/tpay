#!/bin/sh

export connected="no"
while [ $connected = "no" ]
do
  mysql \
    -u$MYSQL_USER -p$MYSQL_PASSWORD -h$MYSQL_HOSTNAME \
    -e "show tables;" $MYSQL_DATABASE
  if [ $? -eq 0 ] ; then
    export connected="yes"
  fi
  sleep 1
done

python manage.py makemigrations
python manage.py migrate

exec "$@"
