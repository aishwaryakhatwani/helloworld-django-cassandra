# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

import time
import datetime
from .models import ExampleModel


# Create your views here.
def helloworld(request):
    return HttpResponse('Hello World')

def create(request):
    ExampleModel.create(example_type=0, description="example1", created_at=datetime.datetime.now())
    output = str(list(ExampleModel.objects.all()))
    output += 'current time = %s' % time.time()
    return HttpResponse(output)
