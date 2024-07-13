from datetime import datetime
from django.shortcuts import render

from booking.models import Client_booking, Hotel
from booking.filters import BookingFilter, HotelFilter
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from booking.serializers import BookingListSerializer, HotelSerializer
from rest_framework.response import Response

# Create your views here.

# use the below function for hotels list
class HotelList(ListAPIView):
    # permission_classes = [IsAuthenticated]
    filterset_class = HotelFilter
    serializer_class = HotelSerializer
    
    def get_queryset(self):
        return (
            Hotel.objects.filter(available= True).order_by("-id")
        )
        
# use the below function for client booking hotels list
class BookingList(ListAPIView):
    permission_classes = [IsAuthenticated]
    filterset_class = BookingFilter
    serializer_class = BookingListSerializer
    
    def get_queryset(self):
        return (
            Client_booking.objects.filter(author_id= self.request.user.id).order_by("-id")
        )
        
# use the below function for client booking hotels
class CreateBooking(CreateAPIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
      end_date=datetime.strptime(request.data.get('end_date'), '%Y-%m-%d')
      start_date=datetime.strptime(request.data.get('start_date'), '%Y-%m-%d')
      days=(end_date-start_date).days + 1
      ht=Hotel.objects.get(id=request.data.get('hotel'))
      cost=days*ht.price_per_day
      Client_booking.objects.create(
                name= str(self.request.user.username)+"-"+str(ht.name),
                cost =  cost,
                days=days,
                start_date=start_date,
                end_date=end_date,
                author_id = request.user.id,
                hotel_id = request.data.get('hotel'),
            )
      return Response(
                {
                    "message" : "Booking is successfull"
                }, status=status.HTTP_200_OK
            )

