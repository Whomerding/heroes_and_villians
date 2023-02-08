

from rest_framework import serializers
from .models import Supers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['type']