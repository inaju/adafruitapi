from rest_framework import serializers
from .models import ElectricityDetail


class ElectricityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElectricityDetail
        fields = '__all__'