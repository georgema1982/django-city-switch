'''
Created on 2011-07-09

@author: George
'''
from django import template
from cities.models import City
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.conf import settings

register = template.Library()

@register.inclusion_tag('city_switch/switch_city_button.html', takes_context=True)
def switch_city_button(context, current_city, next = None):
    country = current_city['region']['country']
    key = country['code'] + '_top_40_cities'
    cities = cache.get(key)
    if not cities:
        cities = []
        for city in City.objects.filter(region__country__pk = country['id']).order_by('-population')[:40]: cities.append({
            'id': city.pk,
            'name': city.name,
            'slug': city.slug,
            'initial': city.slug[0].upper(),
        })
        cache.set(key, cities, settings.SELECT_CITY_CACHE_TIMEOUT)
    return {
        'other_cities': cities,
        'current_city': current_city,
        'next': next,
        'select_city_url': reverse(settings.SELECT_CITY_URL)
    }

@register.inclusion_tag('city_switch/switch_city_button.html', takes_context=True)
def switch_city_button_with_next(context, current_city):
    return switch_city_button(context, current_city, context['request'].path)

@register.inclusion_tag('city_switch/render_select_city.html', takes_context=True)
def render_select_city(context):
    return {
        'cities': context['cities'],
        'countries': context['countries'],
        'current_country': context['current_country'],
    }