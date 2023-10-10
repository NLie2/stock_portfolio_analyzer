from .common import TradetableSerializer


from trades.serializers.common import TradeSerializer


class PopulatedTradestableSerializer(TradetableSerializer):
    trades = TradeSerializer(many=True)
