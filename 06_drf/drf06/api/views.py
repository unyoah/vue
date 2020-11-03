from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.authentication import JWTAuthentication
from api.filters import ComputerFilterSet
from api.models import Computer
from serializers import UserModelSerializer, ComputerModelSerializer
from api.paginations import *


class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        return Response('ok')


class LoginAPIView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            "token": serializer.token,
            "user": UserModelSerializer(serializer.obj).data
        })


class ComputerListAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'price']
    ordering = ['price']

    pagination_class = MyPageNumberPagination

    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination
    filter_class = ComputerFilterSet
