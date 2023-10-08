from rest_framework.generics import  (
  GenericAPIView, 
  RetrieveUpdateDestroyAPIView
)
from lib.views import UserListCreateAPIView

# Models
from .models import Networth

# Serializers
from .serializers.common import NetworthSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly

class NetworthView(GenericAPIView):
  pass

class NetworthListView( NetworthView, UserListCreateAPIView):
  permission_classes= [IsAuthenticated]