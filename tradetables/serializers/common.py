from rest_framework import serializers
from ..models import Tradetable

from trades.models import Trade


class TradetableSerializer(serializers.ModelSerializer):
  class Meta: 
    model = Tradetable
    fields = '__all__'
