from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets

from .filters import ShopFieldsFilter
from .models import City, Shop, Street
from .serializers import CitySerializer, ShopSerializer, StreetSerializer


class CitiesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city = get_object_or_404(City, pk=self.kwargs.get('city_id'))
        return Street.objects.filter(city=city)


class ShopViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    filterset_class = ShopFieldsFilter
