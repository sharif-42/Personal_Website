# Personal_Website

## Create env file
Create an env file named .end.dev in the root directory
```shell
DEBUG=1
SECRET_KEY=secret_key
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]

SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=postgres
SQL_USER=postgres
SQL_PASSWORD=postgres
DATABASE=postgres
SQL_HOST=db
SQL_PORT=5432
```

## Run the project in docker
```shell
docker-compose build
docker-compose up
```

## Apply Migrations
```shell
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

## Create Super User
```shell
docker-compose exec web python manage.py createsuperuser
```