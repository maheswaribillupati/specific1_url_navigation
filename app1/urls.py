from django.urls import path
from app1.views import *
app_name='app1'
urlpatterns=[
    path('bindu/',bindu,name='bindu'),
    path('mahitha/',mahitha,name='mahitha'),
]