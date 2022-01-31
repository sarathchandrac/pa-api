# pa-api
Portfolio Analysis
## Installation
```commandline
docker-compose build
docker-compose up
```
## Run Tests
```commandline
 docker-compose run app sh -c "python manage.py test && flake8"
```

## Create superuser
* login to the service container and run the below command
```commandline
python manage.py createsuperuser
```