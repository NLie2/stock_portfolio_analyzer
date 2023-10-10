from rest_framework import serializers
from ..models import Tradetable


class TradetableSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Tradetable
    fields = '__all__'