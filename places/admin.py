from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from places.models import Municipality, Region


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name',)


admin.site.register(Region, RegionAdmin)


class MunicipalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'is_active')
    search_fields = ('name',)


admin.site.register(Municipality, MunicipalityAdmin)


admin.site.site_header = 'Talenta 365'
admin.site.index_title = 'With Great Power Comes Great Responsibility'

admin.site.unregister(Group)
admin.site.unregister(get_user_model())
