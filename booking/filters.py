import django_filters

from booking.models import Client_booking, Hotel

class HotelFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name",lookup_expr="icontains")
    location = django_filters.CharFilter(field_name="location__name",lookup_expr="icontains")
    

    class Meta:
        model = Hotel
        fields = ("id","name")
        
class BookingFilter(django_filters.FilterSet):
    hotel_name = django_filters.CharFilter(field_name="hotel__name",lookup_expr="icontains")
    class Meta:
        model = Client_booking
        fields = ("id","hotel_name")