from django.urls import path, include
from .views import *

urlpatterns = [
    path('get/', ElectricityListView.as_view(), name="list_get"),
    path('post/', ElectricityCreateView.as_view(), name="list_post"),
]
