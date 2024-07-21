from rest_framework import serializers

from .models import City, Shop, Street


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.PrimaryKeyRelatedField(source='city.name',
                                              queryset=City.objects)
    street = serializers.PrimaryKeyRelatedField(source='street.name',
                                                queryset=Street.objects)
    class Meta:

        model = Shop
        fields = '__all__'

    def get_is_open(self, obj: Shop):
        return obj.is_open

    def create(self, validated_data):
        print(validated_data)
        validated_data['city'] = validated_data.pop('city')['name']
        validated_data['street'] = validated_data.pop('street')['name']
        return Shop.objects.create(**validated_data)


class StreetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Street
        fields = '__all__'
