import re

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from api.models import User, Computer


class UserModelSerializer(ModelSerializer):
    account = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["account", 'password', 'username', 'phone', 'email']
        extra_kwargs = {
            "username": {"read_only": True},
            "phone": {"read_only": True},
            "email": {"read_only": True},

        }

    def validate(self, attrs):
        account = attrs.get("account")
        password = attrs.get("password")
        if re.match(r'1[3-9][0-9]{9}', account):
            user_obj = User.objects.filter(phone=account).first()
        elif re.match(r'.+@.+', account):
            user_obj = User.objects.filter(email=account).first()
        else:
            user_obj = User.objects.filter(username=account).first()
        if user_obj and user_obj.check_password(password):
            payload = jwt_payload_handler(user_obj)
            token = jwt_encode_handler(payload)
            self.obj = user_obj
            self.token = token
        return attrs


class ComputerModelSerializer(ModelSerializer):
    class Meta:
        model = Computer
        fields = "__all__"
