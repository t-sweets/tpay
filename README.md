# t-pay-api

## Setup
```shell
$ docker-compose build
$ docker-compose up                                         # とりあえず起動

$ docker-compose run tpay python manage.py migrate          # DB migrate
$ docker-compose run tpay python manage.py createsuperuser  # SuperUser作成

$ docker-compose up -d                                      # Start
```
