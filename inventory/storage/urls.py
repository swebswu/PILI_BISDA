from django.conf.urls import url
from .views import *


urlpatterns = [

    url(r'^$', index, name='index'),

    url(r'^display_laptops$', display_laptops, name='display_laptops'),
    url(r'^display_desktops$', display_desktops, name='display_desktops'),
    url(r'^display_phones$', display_phones, name='display_phones'),

]