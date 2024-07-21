from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from api.views import CitiesViewSet, ShopViewSet, StreetsViewSet

cityshop_router = DefaultRouter()
cityshop_router.register(r'city', CitiesViewSet)
cityshop_router.register(r'city/(?P<city_id>[\d]+)/street',
                         StreetsViewSet, basename='city_streets')
cityshop_router.register(r'shop', ShopViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'', include(cityshop_router.urls)),
]
