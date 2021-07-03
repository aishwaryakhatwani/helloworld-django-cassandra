# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from cassandra.cluster import Cluster

import time
import datetime
from .models import ExampleModel
from .ConnectCass import Connect
from cassandra.cluster import Cluster

obj = Connect()

# Create your views here.
def displayQueries(request):
    # session.execute("Use killrweather")
    # obj.query1()
    return render(request, 'index.html')

def create(request):
    ExampleModel.create(example_type=0, description="example1", created_at=datetime.datetime.now())
    output = str(list(ExampleModel.objects.all()))
    output += 'current time = %s' % time.time()
    return HttpResponse(output)

def getQuery1(request):
    year = request.POST['quantity']
    data = obj.query1(year)
    
    context = {}
    context['data'] = data
    return render(request, 'query1.html', context)
