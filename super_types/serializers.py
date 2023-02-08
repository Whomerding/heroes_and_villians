

from rest_framework import serializers
from .models import SuperType

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuperType
        fields = ['type']

