# Reservas de Hoteles

Proyecto reservas

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

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


## EndPoints disponibles

(GET) [Listado de habitaciones](http://localhost:8000/api/v1/rooms/).

(POST) [Creacion de reservas](http://localhost:8000/api/v1/bookings/).

    Body example
    {
        "check_in_date": "2022-03-25",
        "payment_method": "TRA",
        "check_out_date": "2022-03-25",
        "room": "5",
        "state": "PAG",
        "customer": {
            "dni": "6828792",
            "bill_to": "Quispe",
            "first_name": "Juan",
            "last_name": "Garcia"
        }
    }

    {
        "check_in_date": "2022-03-25",
        "check_out_date": "2022-03-25",
        "room": "1",
        "customer": {
            "dni": "12351367842",
            "bill_to": "Lopez"
        }
    }

(PUT) [Listado de habitaciones](http://localhost:8000/api/v1/bookings/).

    Body example
    {
        "customer": "6828793",
        "booking": "d902295a-cef0-4b5b-a3a4-607a4c1e9746"
    }
### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

docker-compose run --rm django python manage.py makemigrations

