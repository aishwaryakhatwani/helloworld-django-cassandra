# Weather Data Cassandra Application

## Install virtualenv
```
python3 -m pip install --user virtualenv
```

## Create Virtual environment
```
python3 -m venv env
```

## Activate virutal environment
```
source env/bin/activate
```
## Install Django
```
pip install django
```

## Install cassandra
```
pip install cassandra-driver
```

## Install django-cassandra-engine
```
pip install django-cassandra-engine
```

## Clone this repo
```
git clone url
```

## To Run application
```
cd helloworld-django-cassandra
cd Weather_data
```

## Init Cassandra Keyspace and Table
```
python manage.py sync_cassandra
```

## Startup Web Server
```
python manage.py runserver
```

## Endpoints

* go to http://127.0.0.1:8000/queries -> Start up page that displays the possible queries and takes input from the user.
* go to http://127.0.0.1:8000/query1Results -> Displays Query1 results 
* go to http://127.0.0.1:8000/query2Results -> Displays Query2 results 

## Phase 1: 

```
A django application that uses the killrweather data in Cassandra. The application makes a connection to the Cassandra cluster and uses the killrweather dataset. We use django-cassandra-engine for the communication between the application and Cassandra database. The user is presented with two queries for which they can provide inputs. 
__Query1__: Select max(temperature) as temp, max(dewpoint) as dew, max(pressure) as pressure, max(wind_speed) as wind from raw_weather_data where year = year_input ALLOW FILTERING;
In query1, the user can input a year for which they would like the max temperature, dewpoint, pressure and wind_speed.

__Query2__: Select max(temperature) as temp from raw_weather_data where year = year_input and month = month_input and wsid = weather_stationId_input group by day ALLOW FILTERING; 
In query2, the user can input a year, month and weather station for all the days of the month.
```


