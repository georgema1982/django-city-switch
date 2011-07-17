'''
Created on 2011-06-19

@author: George
'''
from django.utils.importlib import import_module
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse

class SwitchCityMiddleware(object):
    
    def __init__(self):
        self.backend = import_module(settings.SWITCH_CITY_BACKEND)
    
    def process_view(self, request, view, args, kwargs):
        session = request.session
        city = session.get('current_city')
        request.set_city = False
        if not city:
            city = request.COOKIES.get('current_city')
            if city: session['current_city'] = self.backend.get_city(city)
            else:
                city = self.backend.init_city(request)
                if city:
                    session['current_city'] = city
                    request.set_city = True
                else: return redirect_to(request, reverse(settings.SELECT_CITY_URL))
        request.current_city = session['current_city']
        return None
    
    def process_response(self, request, response):
        if hasattr(request, 'set_city') and request.set_city: response.set_cookie('current_city', self.backend.city_key(request.session['current_city']))
        return response
