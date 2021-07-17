from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
import matplotlib.pyplot as plt
import pandas as pd

class Connect:

    __slot__ = 'cluster', 'session'

    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.session.execute('use killrweather')

    def query1(self, year):
        query = 'select max(temperature) as temp, max(dewpoint) as dew, max(pressure) as pressure, max(wind_speed) as wind from raw_weather_data where year=' + year + ' ALLOW FILTERING;'
        print(query)
        statement = SimpleStatement(query)
        data = {}
        
        try:
            for air_base_data in self.session.execute(statement):
                data['Maximum temperature'] = air_base_data[0]
                data['Maximum dewpoint'] = air_base_data[1]
                data['Maximum pressure'] = air_base_data[2]
                data['Maximum wind'] = air_base_data[3]
        except:
            return data
        
        return data

    def query2(self, year, month, airbase):
        query = "select max(temperature) as temp from raw_weather_data where year = "+ year+ " and month = " + month + " and wsid = '" + airbase + "' group by day ALLOW FILTERING;"
        print(query)
        try:
            statement = SimpleStatement(query)
            data = self.session.execute(statement)
        except:
            return []
        return data


    def query3(self, year, station): 
        query = "Select month, AVG(pressure) from raw_weather_data where year = " + year + " and wsid = '" + station + "' group by month ALLOW FILTERING;"
        print(query)
        data = []
        statement = SimpleStatement(query)
        try:
            for pressure in self.session.execute(statement):
                temp = {}
                temp['month'] = pressure[0]
                temp['pressure'] = pressure[1]
                data.append(temp)
            print(data)

            fig = plt.figure()

            plt.plot([temp['month'] for temp in data],[temp['pressure'] for temp in data])
                
            fig.savefig('graph.png')

        except Exception as e:
            print(e)
            return []
        return data