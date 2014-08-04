from django.contrib import admin

# Register your models here.

from .models import Location

class LocationAdmin(admin.ModelAdmin):    
    model = Location

    list_display = ('name', 'locuOrFour_id', 'city', 'src_site')
    list_filter = ['city']



admin.site.register(Location, LocationAdmin)