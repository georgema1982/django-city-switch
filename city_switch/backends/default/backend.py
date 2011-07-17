'''
Created on 2011-06-25

@author: George
'''
from cities.models import City
from city_switch.pyipinfodb import IPInfo
from django.conf import settings
from django.contrib.gis.geos.point import Point
    
def build_city(city):
    country, region, city = city.hierarchy
    return {
        'id': city.pk,
        'name': city.name,
        'slug': city.slug,
        'location': {
            'x': city.location.x,
            'y': city.location.y,
        },
        'region': {
            'id': region.pk,
            'name': region.name,
            'slug': region.slug,
            'code': region.code,
            'country': {
                'id': country.pk,
                'name': country.name,
                'code': country.code,
                'tld': country.tld,
            }
        }
    }
    
def get_city(city):
    return build_city(City.objects.get(pk = city))
    
def init_city(request):
    city = IPInfo(settings.IPINFODB_APIKEY).GetCity(settings.DEBUG and hasattr(settings, 'INTERNAL_IPS') and len(settings.INTERNAL_IPS) and settings.INTERNAL_IPS[0] or request.META['REMOTE_ADDR'])
    if city['statusCode'] != 'OK': return None
    query = City.objects.distance(Point(float(city['latitude']), float(city['longitude']))).filter(name = city['cityName'].title())
    if hasattr(settings, 'COUNTRY_CODES'): query = query.filter(region__country__code__in = settings.COUNTRY_CODES)
    city = query.order_by('distance')[0]
    if not city: return None
    return build_city(city)
    
def city_key(city):
    return city['id']
