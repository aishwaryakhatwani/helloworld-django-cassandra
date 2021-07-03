from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

class Connect:

    __slot__ = 'cluster', 'session'

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.session.execute('use killrweather')

    def query1(self, year):
        statement = SimpleStatement('select max(temperature) as temp, max(dewpoint) as dew, max(pressure) as pressure, max(wind_speed) as wind from raw_weather_data where year=' + year + ' ALLOW FILTERING;')
        data = {}
        
        for air_base_data in self.session.execute(statement):
            data['max_temp'] = air_base_data[0]
            data['max_dewpoint'] = air_base_data[1]
            data['max_pressure'] = air_base_data[2]
            data['max_wind'] = air_base_data[3]
        
        return data

    def query2(self, year, month, airbase):
        query = "select temperature as temp from raw_weather_data where year = "+ year+ " and month = " + month + " and wsid = '" + airbase + "' ALLOW FILTERING;"
        print(query)
        statement = SimpleStatement(query)
        data = self.session.execute(statement)
        print(data)
        return data
