# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.views import registrar_datos

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('registerData/', registrar_datos, name='registrar_datos'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
