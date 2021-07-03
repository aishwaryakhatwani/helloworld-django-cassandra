from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

class Connect:

    __slot__ = 'cluster', 'session'

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.session.execute('use killrweather')

    def query1(self):
        statement = SimpleStatement('select max(temperature) as temp, max(dewpoint) as dew, max(pressure) as pressure, max(wind_speed) as wind from raw_weather_data where year=2014 ALLOW FILTERING;')
        data = {}
        
        for air_base_data in self.session.execute(statement):
            data['temp'] = air_base_data[0]
            data['dewpoint'] = air_base_data[1]
            data['pressure'] = air_base_data[2]
            data['wind'] = air_base_data[3]
        
        return data

    def query2(self):
        statement = SimpleStatement('select * from raw_weather_data limit 3;')
        for user_row in self.session.execute(statement):
            print(user_row)
