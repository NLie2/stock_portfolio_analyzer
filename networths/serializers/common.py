from rest_framework import serializers
from ..models import Networth


class NetworthSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Networth
    fields = '__all__'