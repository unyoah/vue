from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from api.models import User


class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        auth = request.META.get("HTTP_AUTHORIZATION", None)
        if auth is None:
            return None
        auto_split = auth.split()
        if not (len(auto_split) == 2 and auto_split[0].lower() == "auth"):
            raise exceptions.AuthenticationFailed('信息有误')
        if auto_split[1] != 'aaa.admin.bbb':
            raise exceptions.AuthenticationFailed('认证失败')
        user = User.objects.filter(username="admin").first()

        if not user:
            raise exceptions.AuthenticationFailed("用户不存在或已被删除")
        return user, None
