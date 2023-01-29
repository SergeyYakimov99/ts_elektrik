from rest_framework import serializers

from ts_elektrik.models import Factory, Retail_network, Sole_trader


class FactorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class Retail_networkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail_network
        fields = '__all__'


class Sole_traderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sole_trader
        fields = '__all__'
