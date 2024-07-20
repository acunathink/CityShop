from rest_framework import serializers

from .models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = '__all__'

    def get_is_open(self, obj: Shop):
        return obj.is_open


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = '__all__'
