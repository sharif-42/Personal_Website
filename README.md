# Personal_Website

## Run the project in docker
```shell
docker-compose build
docker-compose up
```

## Apply Migrations(run sequentially)
```shell
docker-compose run web sh 
python manage.py makemigrations
python manage.py migrate
```

## Create Super User
```shell
docker-compose run web sh
python manage.py createsuperuser
```