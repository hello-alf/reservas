# Reservas

Proyecto reservas

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Comandos básicos

### Instalando el proyecto

Una vez clonado el proyecto ejecutar los siguientes comandos

    $ docker-compose -f local.yml build
    $ docker-compose -f local.yml up -d

### Corriengo migraciones

Para ejecutar las migraciones correspondientes hacia la base de datos:

    $ docker-compose -f local.yml run --rm django python manage.py migrate

### Corrigendo fixtures

Ejecutar los fixtures para llenar los estados y los métodos de pago iniciales

    $ docker-compose -f local.yml run --rm django python manage.py loaddata payment_method_fixture
    $ docker-compose -f local.yml run --rm django python manage.py loaddata state_fixture

#### Running tests with pytest

    $ pytest

### Live reloading and Sass CSS compilation

Moved to [Live reloading and SASS compilation](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally.html#sass-compilation-live-reloading).

## Deployment

The following details how to deploy this application.

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

docker-compose run --rm django python manage.py makemigrations

