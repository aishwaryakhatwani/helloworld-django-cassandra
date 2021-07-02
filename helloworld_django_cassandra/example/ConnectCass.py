from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

class Connect:

    __slot__ = 'cluster', 'session'

    def __init__(self):
        self.cluster = Cluster(protocol_version=3)
        self.session = self.cluster.connect()
        self.session.execute('use killrweather')

    def query1(self):
        statement = SimpleStatement('select max(temperature), max(dewpoint), max(pressure), max(wind_speed) from raw_weather_data where year=2014 ALLOW FILTERING;')
        for user_row in self.session.execute(statement):
            print(user_row)

    def query2(self):
        statement = SimpleStatement('select * from raw_weather_data limit 3;')
        for user_row in self.session.execute(statement):
            print(user_row)
