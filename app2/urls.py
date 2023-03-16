from django.urls import path
from app2.views import *
app_name='app2'
urlpatterns=[
    path('madhusri/',madhusri,name='madhusri'),
    path('srividya/',srividya,name='srividya'),
]