# Create your views here.
from django.views.generic.simple import redirect_to
from django.conf import settings
from django.utils.importlib import import_module

get_city = import_module(settings.SWITCH_CITY_BACKEND).get_city

def switch_city_to(request, city):
    request.current_city = request.session['current_city'] = get_city(city)
    request.set_city = True
    return redirect_to(request, request.REQUEST.get('next') or '/')
