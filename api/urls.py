from django.urls import path, include
from .views import *

urlpatterns = [
    path('get/', ElectricityDetailView.as_view(), name="list_create"),
]
