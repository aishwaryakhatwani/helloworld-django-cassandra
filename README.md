# helloworld-django-cassandra

This is a simple hello world boilerplate project that demonstrates the use of cassandra as database backend

## Install django-cassandra-engine
```
pip install django-cassandra-engine
```

## Init Cassandra Keyspace and Table
```
python manage.py sync_cassandra
```

## Startup Web Server
```
python manage.py runserver
```

## Hello World

go to http://127.0.0.1:8000/helloworld -> Hello World will be returned
go to http://127.0.0.1:8000/create -> A test record will be created and a list of all test records will display as well as the current timestamp

