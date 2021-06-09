from django.shortcuts import render
from .models import ElectricityDetail
from .serializers import ElectricityDetailSerializer
from rest_framework import generics
# Create your views here.

class ElectricityDetailView(generics.ListCreateAPIView):
    queryset = ElectricityDetail.objects.all()
    serializer_class = ElectricityDetailSerializer