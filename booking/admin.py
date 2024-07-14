from django.contrib import admin

from booking.models import Client_booking, Hotel, Location

# Register your models here.

class LocationAdmin(admin.ModelAdmin):
    # form = HotelForm
    search_fields = ["name"]
    list_display = [f.name for f in Location._meta.fields]
    date_hierarchy = "created"
    
class Client_bookingAdmin(admin.ModelAdmin):
    # form = HotelForm
    list_display = [f.name for f in Client_booking._meta.fields]
    date_hierarchy = "created"
    
class HotelAdmin(admin.ModelAdmin):
    # form = HotelForm
    search_fields = ["name"]
    list_display = [f.name for f in Hotel._meta.fields]
    date_hierarchy = "created"
    autocomplete_fields = ["location","author"]
    
admin.site.register(Location, LocationAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Client_booking, Client_bookingAdmin)