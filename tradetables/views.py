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

from lib.eod_request import get_prices, get_dividents

class TradeTableView(GenericAPIView ):
  queryset=Tradetable.objects.all()
  serializer_class=TradetableSerializer

class TradetableListView(TradeTableView, CreateAPIView):
  permission_classes = [IsAuthenticated, IsOwner]

  #overwrite create method because I want users to be able to create nested tables
  def create(self, request):

    
    
    trade_table = request.data.get('trade_table')
    trades= request.data.get('trades')

    # get dates and tickers from request, and make sure there are no duplicates 
    dates = [ trade['date'] for trade in trades]
    date_from = min(dates) # You can also specify a maximum date but default is today. 

    tickers = list(dict.fromkeys([ trade['ticker'] for trade in trades]))

    #get prices and dividents
    # ! Not getting dividents right now because of an error and because it is not necesary for the MVP, which only determines networth
    # dividents = get_dividents(date_from=date_from, tickers=tickers)
    prices = get_prices(date_from=date_from, tickers=tickers)


    serialized_tradetable = TradetableSerializer(data=trade_table)

    if serialized_tradetable.is_valid():

      serialized_tradetable.save(user=self.request.user)
      print("All trades... ", trades)

      #map trades to include the serialized table id
      for trade in trades: 
        trade['tradeTable'] = serialized_tradetable.data['id']
        print("INDIVIDUAL TRADE...", trade)
        serialized_trade = TradeSerializer(data=trade)
        print(serialized_trade.is_valid())

        if serialized_trade.is_valid():
          serialized_trade.save()
    
        else: 
          return Response('Serialized trade is not valid')
    
      # ! Do not return dividents
      # return Response({'prices': prices, 'dividents': dividents, 'trades': trades})

      return Response({'prices': prices, 'trades': trades})
    else:
      return Response('serialized trade table is not valid')



class TradetableDetailView(TradeTableView, RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, IsOwner]
  serializer_class=PopulatedTradestableSerializer


