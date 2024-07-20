from django.contrib import admin

from .models import City, Shop, Street


class StreetAdmin(admin.ModelAdmin):
    list_display = 'name', 'city'
    list_filter = 'city',
    search_fields = 'name',


class ShopAdmin(admin.ModelAdmin):
    list_display = 'name', 'city', 'street', 'open_time', 'close_time'
    list_filter = 'city', 'street', 'open_time', 'close_time'
    search_fields = 'name',
    list_editable = 'open_time', 'close_time'
    sortable_by = 'city', 'street', 'open_time', 'close_time'


admin.site.register(City)
admin.site.register(Street, StreetAdmin)
admin.site.register(Shop, ShopAdmin)
