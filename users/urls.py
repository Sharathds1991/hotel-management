from django.urls import path

from users.views import (
    CustomerLogin,Client_Registration,
)
from knox import views as knox_views

urlpatterns = [
    path("client/login/", CustomerLogin.as_view()),
    path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("client/registration/", Client_Registration.as_view()),

]

