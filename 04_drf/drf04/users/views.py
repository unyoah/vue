from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin

# Create your views here.
from users.models import User
from users.serializers import UserModelSerializer


class UserView(GenericViewSet, GenericAPIView, CreateModelMixin):
    queryset = User.objects.filter()
    serializer_class = UserModelSerializer

    def user_register(self, request, *args, **kwargs):
        request_data = request.data
        if request_data.get('password')!=request_data.pop('re_password'):
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '注册失败',
            })
        serializer = self.get_serializer(data=request_data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': '成功注册',
            'results': self.get_serializer(user).data
        })

    def user_login(self, request, *args, **kwargs):
        request_data = request.data
        try:
            user_obj = User.objects.get(user_name=request_data.get('user_name'), password=request_data.get('password'))
        except User.DoesNotExist:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '用户名或密码不正确'
            })
        serializer = self.get_serializer(user_obj).data
        return Response({
            'status': status.HTTP_200_OK,
            'message': '登录成功',
            'results': serializer
        })
