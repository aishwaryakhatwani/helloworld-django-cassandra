"""helloworld_django_cassandra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the incude() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from example import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^queries', views.displayQueries),
    url(r'^create', views.create),
    url(r'^query1/<int:year>/', views.getQuery1, name='getQuery1')
    # path('index', views.getQuery1)
]
