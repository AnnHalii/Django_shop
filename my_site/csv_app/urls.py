from django.urls import path
from .views import *

urlpatterns = [
    path('download/', GenerateCSV.as_view(), name='generate_csv'),
]