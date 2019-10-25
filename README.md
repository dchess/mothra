# mothra
Web app for collecting and sharing education system usage among Data Whiz members

## Dependencies

* Python3.7
* Django 2.2
* [Pipenv](https://pipenv.readthedocs.io/en/latest/)
* [Docker](https://www.docker.com/)

## Getting Started

### Setup Environment

1. Clone this repo

```
$  git clone https://github.com/dchess/mothra.git
```

2. Install Pipenv

```
$ pip install pipenv
```

3. Install Docker

* [Mac](https://docs.docker.com/docker-for-mac/install/)
* [Linux](https://docs.docker.com/install/linux/docker-ce/debian/)
* [Windows](https://docs.docker.com/docker-for-windows/install/)

4. Create .env file with project secrets

**dev environment**
```
SECRET_KEY=
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DB=
```


Generating a unique secret key can be done via Django:

```python
from django.core.management.utils import get_random_secret_key 
get_random_secret_key()
```

5. Build Docker Image

```
$ docker-compose build
```

### Running the Server

**dev environment**
```
$ docker-compose up -d
```

### Running Database Migrations

```
$ docker-compose run web python manage.py migrate
```

### Create a superuser

```
$ docker-compose run web python manage.py createsuperuser
```

### Taking the server down

```
$ docker-compose down
```

### Running Tests

```
$ docker-compose exec web pytest
```

## Documentation

A fulll tutorial documenting the creation of this app is available in [the wiki](https://github.com/dchess/mothra/wiki).