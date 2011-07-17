from city_switch.utils import inject_app_defaults

inject_app_defaults(__name__)

from city_switch import urls as main_urls
from django.conf import settings as prj_settings
from city_switch.backends.default.urls import urlpatterns

if prj_settings.CITY_SWITCH_DEFAULT_BACKEND_URL_AUTO_SETUP: main_urls.urlpatterns += urlpatterns