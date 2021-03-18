from django.urls import path

from .views import *



urlpatterns=[
    path('game/create/', GameCreate.as_view(), name='company_list'),
]