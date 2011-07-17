'''
Created on 2011-07-15

@author: George
'''
from cities.models import City, Country
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from django.views.decorators.cache import cache_page

@cache_page(settings.SELECT_CITY_CACHE_TIMEOUT)
def select_city(request, template, country = None):
    if not country: country = settings.COUNTRY_CODES[0]
    cities = []
    query = City.objects.filter(region__country__code = country)
    min_pop = settings.MIN_POPULATION_FOR_COUNTRY.get(country)
    if min_pop: query = query.filter(population__gte = min_pop) 
    for city in query: cities.append({
        'id': city.pk,
        'name': city.name,
        'slug': city.slug,
        'initial': city.slug[0].upper(),
    });
    return render_to_response(template, {
        'cities': cities,
        'countries': Country.objects.filter(code__in = settings.COUNTRY_CODES).order_by('name'),
        'current_country': Country.objects.get(code = country),
    }, context_instance = RequestContext(request))
