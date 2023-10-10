from rest_framework.generics import  (
  GenericAPIView, 
  RetrieveUpdateDestroyAPIView
)
from lib.views import UserListCreateAPIView

# Models
from .models import Tradetable
# Serializers
from .serializers.common import TradetableSerializer
from .serializers.populated import PopulatedTradestableSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly, IsOwner

class TradeTableView(GenericAPIView ):
  queryset=Tradetable.objects.all()
  serializer_class=PopulatedTradestableSerializer

class TradetableListView(TradeTableView, UserListCreateAPIView):
  permission_classes = [IsAuthenticated, IsOwner]


class TradetableDetailView(TradeTableView, RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, IsOwner]


