FROM nginx:1.15-alpine

RUN rm -f /etc/nginx/conf.d/*

COPY tpay_nginx.conf /etc/nginx/conf.d/tpay_nginx.conf
COPY front_nginx.conf /etc/nginx/conf.d/front_nginx.conf
COPY uwsgi_params /etc/nginx/uwsgi_params
COPY docker-entrypoint.sh /usr/bin/

RUN chmod 755 /usr/bin/docker-entrypoint.sh
RUN mkdir -p /tpay_static
RUN mkdir -p /tpay_media
RUN mkdir -p /tpay_front

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["nginx", "-g", "daemon off;"]
