from django.contrib import admin

from places.models import Municipality, Region

admin.site.register(Region)
admin.site.register(Municipality)