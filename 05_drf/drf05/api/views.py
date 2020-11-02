from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api.authentications import MyAuth
from api.permission import MyPermission
from api.throttle import SendMessageRate


class UserAPIView(APIView):
    authentication_classes = [MyAuth]
    permission_classes = [MyPermission]
    throttle_classes = [SendMessageRate]
    def get(self, request, *args, **kwargs):
        print("get")
        return Response('get')

    def post(self, request, *args, **kwargs):
        print("post")
        return Response('post')
