from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken

from api import views

urlpatterns = [
    path("login/", ObtainJSONWebToken.as_view()),
    path("detail/", views.UserDetailAPIView.as_view()),
    path("user/", views.LoginAPIView.as_view()),
    path("computer/", views.ComputerListAPIView.as_view()),
]
