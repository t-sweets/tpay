#!/bin/sh
sed -i "s/UWSGI_HOST/$UWSGI_HOST/g" /etc/nginx/conf.d/tpay_nginx.conf
exec "$@"
