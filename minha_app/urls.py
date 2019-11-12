# coding: utf-8

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index',),
    url('^accounts/profile/$', views.profile, name='profile',),
]
