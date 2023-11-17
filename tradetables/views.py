# packages
import json

# ret framework

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

#Files and assets
from lib.eod_request import get_prices, get_dividents, get_exchange_rates
from lib.caclulate_networth import convertToEuro, addMissingDates


with open('lib/files/currency_pairs.json', 'r') as json_file:
    currency_pairs = json.load(json_file)

class TradeTableView(GenericAPIView ):
  queryset=Tradetable.objects.all()
  serializer_class=TradetableSerializer

class TradetableListView(TradeTableView, CreateAPIView):
  permission_classes = [IsAuthenticated, IsOwner]

  #overwrite create method because I want users to be able to create nested tables
  # def create(self, request):

    
    
  #   trade_table = request.data.get('trade_table')
  #   trades= request.data.get('trades')

  #   # get dates and tickers from request, and make sure there are no duplicates 
  #   dates = [ trade['date'] for trade in trades]
  #   date_from = min(dates) # You can also specify a maximum date but default is today. 

  #   tickers = list(dict.fromkeys([ trade['ticker'] for trade in trades]))

  #   #get prices and dividents
  #   # ! Not getting dividents right now because of an error and because it is not necesary for the MVP, which only determines networth
  #   # dividents = get_dividents(date_from=date_from, tickers=tickers)
  #   prices = get_prices(date_from=date_from, tickers=tickers)

  #   # Get currency exchange rates
  #   currency_exchange_rates = get_exchange_rates( date_from=date_from, currency_pairs= currency_pairs )
  #   # print(currency_exchange_rates)

  #   # ! calculate_networth here 
  #   prices_eur = convertToEuro(trades, prices)
  #   print("PRICES EUR", convertToEuro(trades, prices))

  #   # input: price table, output, networth table 

  #   # Next step: save the networth table as a model ‚

  #   serialized_tradetable = TradetableSerializer(data=trade_table)

  #   if serialized_tradetable.is_valid():

  #     serialized_tradetable.save(user=self.request.user)
  #     #print("All trades... ", trades)

  #     #map trades to include the serialized table id
  #     for trade in trades: 
  #       #print(serialized_tradetable.data['id'])
  #       trade['tradeTable'] = serialized_tradetable.data['id']
  #       #print("INDIVIDUAL TRADE...", trade['tradeTable'])
  #       serialized_trade = TradeSerializer(data=trade)
  #       #print(serialized_trade.is_valid())

  #       if serialized_trade.is_valid():
  #         serialized_trade.save()
  #         #print(serialized_trade)
    
  #       else: 
  #         return Response('Serialized trade is not valid')
    
  #     # ! Do not return dividents
  #     print("PRICES...", prices)
  #     print("")
  #     print("TRADES...", trades)
  #     print("")
  #     print("PRRICES_EUR...", prices_eur)

  #     #return Response({'prices': prices, 'trades': trades})
  #     # return Response("done")

  #     # ! Also return networth here 
  #     return Response({'prices': prices.keys(), 'trades': trades[0], 'prices_eur': prices_eur.keys()})
  #   else:
  #     return Response('serialized trade table is not valid')
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

    #Get prices
    prices = get_prices(date_from=date_from, tickers=tickers)

    # Get exchange rates
    exchange_rates = get_exchange_rates(date_from=date_from, currency_pairs=currency_pairs)

    # input: price table, output, networth table 
    prices_eur = convertToEuro(trades, prices, exchange_rates)

    # # add missing rows
    # ! Next step
    prices_eur_full = addMissingDates(prices_eur)

    # Next step: save the networth table as a model ‚


    serialized_tradetable = TradetableSerializer(data=trade_table)

    if serialized_tradetable.is_valid():

      serialized_tradetable.save(user=self.request.user)

      #map trades to include the serialized table id
      for trade in trades: 
        trade['tradeTable'] = serialized_tradetable.data['id']
        serialized_trade = TradeSerializer(data=trade)
        print(serialized_trade.is_valid())

        if serialized_trade.is_valid():
          serialized_trade.save()
    
        else: 
          return Response('Serialized trade is not valid')
    
      # ! Do not return dividents
      # return Response({'prices': prices, 'dividents': dividents, 'trades': trades})

      # ! Also return networth here 
      return Response({'prices': prices, 'trades': trades, 'prices_eur': prices_eur, 'exchange_rates': exchange_rates, 'prices_eur_full': prices_eur_full})
    else:
      return Response('serialized trade table is not valid')



class TradetableDetailView(TradeTableView, RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthenticated, IsOwner]
  serializer_class=PopulatedTradestableSerializer


