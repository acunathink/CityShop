from rest_framework import mixins, viewsets

from .models import City, Shop, Street
from .serializers import CitySerializer, ShopSerializer, StreetSerializer


class CitiesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class ShopViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
