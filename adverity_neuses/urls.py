from django.conf.urls import url, include
from rest_framework import routers
from . import views


"""adverity_neuses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index_alternative'),
    url(r'^task1/$', views.task1, name='task1'),
    url(r'^task2/$', views.task2, name='task2'),
    url(r'^api/task1/$', views.api_task1, name='task1'),
    url(r'^api/task2/$', views.api_task2, name='task2'),
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
