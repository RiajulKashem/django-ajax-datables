# Django Datatables Serverside

[![Python Version](https://img.shields.io/badge/python-3.9-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.2-brightgreen.svg)](https://djangoproject.com)

This is an example project to Django Datatables Server side **pagination, ordering and search** enabled

![List Page](screenshots/data-table.png)
![Detail Page](screenshots/detail.png)

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/RiajulKashem/sapience-trio.git
```

Copy .env.example to .env

```bash
cp .env.example sapience_trio/.env
```

Build docker images

```bash
docker-compose build
```

Start services

```bash
docker-compose up -d --build 
```
View Docker log

```bash
docker-compose logs -f
```
Load Fixtures

```bash
docker-compose run web python manage.py loaddata cart/fixtures/item.json
docker-compose run web python manage.py loaddata cart/fixtures/order.json
docker-compose run web python manage.py loaddata cart/fixtures/order_item.json
```