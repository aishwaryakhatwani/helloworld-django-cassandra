# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from cassandra.cluster import Cluster

import time
import datetime
from .models import ExampleModel
# from .ConnectCass import Connect
from cassandra.cluster import Cluster

# obj = Connect()
# obj.cass()

# Create your views here.
def helloworld(request):
    cluster = Cluster(protocol_version=3)
    session = cluster.connect()
    session.execute("Use killrweather")
    results = session.execute("select * from raw_weather_data limit 3")
    user = results.one()
    print(user)
    return render(request, 'index.html')

def create(request):
    ExampleModel.create(example_type=0, description="example1", created_at=datetime.datetime.now())
    output = str(list(ExampleModel.objects.all()))
    output += 'current time = %s' % time.time()
    return HttpResponse(output)
