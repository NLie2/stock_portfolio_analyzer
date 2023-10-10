from rest_framework.generics import  (
  GenericAPIView, 
  RetrieveUpdateDestroyAPIView
)
from lib.views import UserListCreateAPIView

# Models
from .models import Tradetable
# Serializers
from .serializers.common import TradetableSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly, IsOwner

class TradeTableView(GenericAPIView):
  queryset=Tradetable.objects.all()
  serializer_class=TradetableSerializer
  permission_classes = [IsAuthenticated, IsOwner]


