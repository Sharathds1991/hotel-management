from django.urls import path

from booking.views import HotelList, BookingList,CreateBooking
from users.views import (
    CustomerLogin,Client_Registration,
)
from knox import views as knox_views

urlpatterns = [
    path("hotellist", HotelList.as_view()),
    path("bookinglist", BookingList.as_view()),
    path("createbooking", CreateBooking.as_view()),
    path("client/login/", CustomerLogin.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("client/registration/", Client_Registration.as_view()),

]

