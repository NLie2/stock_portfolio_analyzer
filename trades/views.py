from rest_framework.generics import  (
  GenericAPIView, 
  RetrieveUpdateDestroyAPIView
)
from lib.views import UserListCreateAPIView

# Models
from .models import Trade

# Serializers
from .serializers.common import TradeSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly, IsOwner

class TradeView(GenericAPIView):
  queryset=Trade.objects.all()
  serializer_class=TradeSerializer


# ? Am I going to have to change this to RetrieveUpdateDestroyAPIView as well? 
# ? Because I want to make it possible to upload an entire table at once. 
class TradeListView(TradeView, UserListCreateAPIView ):
  permission_classes = [IsOwner]


# This is going to allow us to add individual trades if we want. 
class TradeDetailView(TradeView, RetrieveUpdateDestroyAPIView):
  permission_classes = [IsOwner]
