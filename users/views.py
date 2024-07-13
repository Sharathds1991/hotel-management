from django.shortcuts import render
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import  Group

from users.models import CustomUser

# Create your views here.

# use the below function for client login
class CustomerLogin(KnoxLoginView):
    """
    Login for Business Developer
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        if user.groups.all().exists():
            if user.groups.filter(name="customer").exists():
                login(request, user)
                d = super(CustomerLogin, self).post(request, format=None)
                d.data["id"] = user.id
                d.data["name"] = str(user.first_name) + " " + str(user.last_name)
                return d
            else:
                return Response(
                    {"message": "Only Client login is allowed! "},
                    status=status.HTTP_400_BAD_REQUEST,
                )
                
# use the below function for client registartion
class Client_Registration(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, *args, **kwargs):
      if  request.data.get('password')== request.data.get('confirm_password'):
        if not CustomUser.objects.filter(username__iexact = request.data.get("username")):
          user = CustomUser.objects.create(username=request.data.get("username"),
                      email=request.data.get('email'),
                      first_name = request.data.get('email'))
          user.set_password( request.data.get('password'))
          group = Group.objects.get(name='customer')
          user.groups.add(group)
          user.save()
          return Response(
                {"message": "Client registered....! "},
                status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": "Client already registered....! "},
                status=status.HTTP_400_BAD_REQUEST)
      else:
            return Response(
                {"message": "Password not matching....! "},
                status=status.HTTP_400_BAD_REQUEST)
