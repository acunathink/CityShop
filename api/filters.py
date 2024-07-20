from datetime import datetime

from django_filters import AllValuesMultipleFilter
from django_filters import rest_framework as filter

from .models import Shop


class ShopFieldsFilter(filter.FilterSet):
    """Класс ShopFieldsFilter используется для добавления возможности
    добавлять к запросам параметры фильтрации и поиска."""

    city = AllValuesMultipleFilter(
        field_name='city__name')
    street = AllValuesMultipleFilter(
        field_name='street__name')
    open = filter.BooleanFilter(method='filter_is_open')

    class Meta:
        model = Shop
        fields = ('city', 'street', 'open')

    def filter_is_open(self, queryset, _, need_open):
        now = datetime.now().time()
        if need_open:
            return queryset.filter(open_time__lte=now, close_time__gte=now)
        else:
            return queryset.exclude(open_time__lte=now, close_time__gte=now)
