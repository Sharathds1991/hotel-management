from django.urls import path

from booking.views import HotelList, BookingList,CreateBooking


urlpatterns = [
    path("hotellist", HotelList.as_view()),
    path("bookinglist", BookingList.as_view()),
    path("createbooking", CreateBooking.as_view()),

]

