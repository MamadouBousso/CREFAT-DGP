# -*- coding: utf-8 -*-
"""
Created on Wed May 13 00:27:31 2015

@author: Khadime_Wade
"""

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^variable$', views.variable, name='variable'),
    url(r'^equation$', views.equation, name='equation'),
    url(r'^parametrage$', views.parametrage, name='parametrage'),
    url(r'^systeme$', views.systeme, name='systeme'),
    url(r'^date$', views.date_actuelle, name='date'),

]