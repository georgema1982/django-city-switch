'''
Created on 2011-07-15

@author: George
'''
from django.conf.urls.defaults import *
from city_switch.backends.default.views import select_city

SELECT_CITY_PARAMS = {'template': 'city_switch/select_city.html'}

urlpatterns = patterns('',
    url(r'^select_city/$', select_city, SELECT_CITY_PARAMS, name = 'go_to_select_city'),
    url(r'^select_city/(?P<country>\w+)/', select_city, SELECT_CITY_PARAMS, name = 'switch_country'),
)

