from rest_framework.viewsets import ModelViewSet

from ts_elektrik.models import Factory, Retail_network, Sole_trader
from ts_elektrik.serializers import FactorySerializer, Retail_networkSerializer, Sole_traderSerializer
#from ts_elektrik.serializers import FactorySerializer


class FactoryViewSet(ModelViewSet):
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class Retail_networkViewSet(ModelViewSet):
    queryset = Retail_network.objects.all()
    serializer_class = Retail_networkSerializer


class Sole_traderViewSet(ModelViewSet):
    queryset = Sole_trader.objects.all()
    serializer_class = Sole_traderSerializer
