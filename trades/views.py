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


class TradeListView(TradeView, UserListCreateAPIView ):
  permission_classes = [IsAuthenticated, IsOwner]


# This is going to allow us to add individual trades if we want. 
class TradeDetailView(TradeView, RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, IsOwner]
