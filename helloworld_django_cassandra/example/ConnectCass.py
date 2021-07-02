from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement

class Connect:

    __slot__ = 'cluster', 'session'

    def __init__(self):
        self.cluster = Cluster(protocol_version=3)
        self.session = self.cluster.connect()

    def cass(self):
        self.session.execute('use killrweather')
        statement = SimpleStatement('select * from raw_weather_data limit 3;')
        for user_row in self.session.execute(statement):
            print(user_row)
