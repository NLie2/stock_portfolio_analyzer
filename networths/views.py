from rest_framework.generics import  (
  GenericAPIView, 
  RetrieveUpdateDestroyAPIView, 
  CreateAPIView
)
from lib.views import UserListCreateAPIView

# Models
from .models import Networth

# Serializers
from .serializers.common import NetworthSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly, IsOwner

class NetworthView(GenericAPIView):
  queryset=Networth.objects.all()
  serializer_class=NetworthSerializer

class NetworthListView( NetworthView, CreateAPIView):
  permission_classes= [IsAuthenticated, IsOwner] 
  def perform_create(self, serializer):
      serializer.save(user=self.request.user)

class NetworthDetailView(NetworthView, RetrieveUpdateDestroyAPIView):
  permission_classes= [IsAuthenticated, IsOwner] 
