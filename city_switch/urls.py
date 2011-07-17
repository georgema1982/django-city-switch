'''
Created on 2011-06-12

@author: George
'''
from django.conf.urls.defaults import *
from city_switch.views import switch_city_to

urlpatterns = patterns('',
    url(r'^switch_city_to/(?P<city>\w+)/', switch_city_to, name = 'switch_city_to'),
)

