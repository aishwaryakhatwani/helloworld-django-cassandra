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
from django.views.decorators.csrf import csrf_exempt

obj = Connect()

# Create your views here.
def displayQueries(request):
    # session.execute("Use killrweather")
    # obj.query1()
    return render(request, 'index.html')

@csrf_exempt
def getQuery1(request):
    year = request.GET['year']
    data = obj.query1(year)
    
    context = {}
    context['data'] = data
    return render(request, 'query1.html', context)

@csrf_exempt
def getQuery2(request):
    year = request.GET['year_2']
    month = request.GET['month']
    airbase = request.GET['airBase']
    data = obj.query2(year, month, airbase)
    
    context = {}
    context['data'] = data
    return render(request, 'query2.html', context)