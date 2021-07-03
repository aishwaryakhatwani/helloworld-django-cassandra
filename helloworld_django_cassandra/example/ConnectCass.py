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
            data['Maximum temperature'] = air_base_data[0]
            data['Maximum dewpoint'] = air_base_data[1]
            data['Maximum pressure'] = air_base_data[2]
            data['Maximum wind'] = air_base_data[3]
        
        return data

    def query2(self, year, month, airbase):
        query = "select max(temperature) as temp from raw_weather_data where year = "+ year+ " and month = " + month + " and wsid = '" + airbase + "' group by day ALLOW FILTERING;"
        print(query)
        statement = SimpleStatement(query)
        data = self.session.execute(statement)
        print(data)
        return data
