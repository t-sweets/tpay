FROM python:3.6-alpine3.8

ENV PYTHONUNBUFFERED 1
ARG project_dir=/app/

ADD requirements.txt $project_dir
WORKDIR $project_dir

RUN apk --no-cache --virtual .requirements add g++ make linux-headers && \
    apk --no-cache add libjpeg jpeg-dev libffi-dev mysql-dev mysql-client && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && rm -rf ~/.cache/pip && \
    apk del .requirements

ADD . $project_dir
COPY docker-entrypoint.sh /usr/bin/
RUN chmod 755 /usr/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["uwsgi", "--ini", "tpay_uwsgi.ini"]
