from django.shortcuts import render
from .models import ElectricityDetail
from .serializers import ElectricityDetailSerializer
from rest_framework import generics
# Create your views here.

class ElectricityListView(generics.ListAPIView):
    queryset = ElectricityDetail.objects.all()
    serializer_class = ElectricityDetailSerializer


class ElectricityCreateView(generics.CreateAPIView):
    queryset = ElectricityDetail.objects.all()
    serializer_class = ElectricityDetailSerializer