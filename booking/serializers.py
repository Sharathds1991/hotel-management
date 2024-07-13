from rest_framework import serializers

from booking.models import Client_booking, Hotel
class HotelSerializer(serializers.ModelSerializer):
    location = serializers.ReadOnlyField(source = "location.name")
    class Meta:
        model = Hotel
        fields = ("id",
            "name",
            "location",
            "description",
            "price_per_day",
            "available",)
        
class BookingListSerializer(serializers.ModelSerializer):
    hotel = serializers.ReadOnlyField(source = "hotel.name")
  
    class Meta:
        model = Client_booking
        fields = ("id",
            "name",
            "cost",
            "days",
            "hotel",
            "start_date",
            "end_date",)