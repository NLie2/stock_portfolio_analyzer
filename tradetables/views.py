from rest_framework.generics import  (
  GenericAPIView, 
  RetrieveUpdateDestroyAPIView, 
  CreateAPIView
)
from lib.views import UserListCreateAPIView

# Models
from .models import Tradetable

# Serializers
from .serializers.common import TradetableSerializer
from .serializers.populated import PopulatedTradestableSerializer
from trades.serializers.common import TradeSerializer

# Permissions
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from lib.permissions import IsOwnerOrReadOnly, IsOwner


# Rest Framework
from rest_framework.response import Response

class TradeTableView(GenericAPIView ):
  queryset=Tradetable.objects.all()
  serializer_class=TradetableSerializer

class TradetableListView(TradeTableView, CreateAPIView):
  permission_classes = [IsAuthenticated, IsOwner]

  #overwrite create method because I want users to be able to create nested tables
  def create(self, request):

    print(request.user)
    trade_table = request.data.get('trade_table')
    trade_table['user'] = request.user.id


    serialized_tradetable = TradetableSerializer(data=trade_table)



    if serialized_tradetable.is_valid():
      serialized_tradetable.save()

      #then trades
      trades= request.data.get('trades')

      print('ID...', serialized_tradetable.data['id'])

      #map trades to include the serialized table id
      for trade in trades: 
        trade['tradeTable'] = serialized_tradetable.data['id']
        

        serialized_trade = TradeSerializer(data=trade)

        print('check out serialized trade...', serialized_trade)
        print('is valid... ', serialized_trade.is_valid())

        if serialized_trade.is_valid():
          serialized_trade.save()
    
        else: 
          return Response('Something went wrong')
      
      return Response(201)
    else:
      return Response('Something went wrong')



class TradetableDetailView(TradeTableView, RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, IsOwner]
  serializer_class=PopulatedTradestableSerializer


