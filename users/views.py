from rest_framework.generics  import (CreateAPIView, RetrieveAPIView)
from .serializers.common import RegistrationSerializer
from django.contrib.auth import get_user_model

from networths.models import Networth

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly, IsOwner

# Rest Framework
from rest_framework.response import Response


User = get_user_model()

class RegisterView(CreateAPIView):
  queryset = User.objects.all()
  serializer_class = RegistrationSerializer



