from rest_framework import serializers, exceptions

from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('user_name', 'password', "re_password")
        extra_kwargs = {

            "user_name": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    "required": "用户名必须提供",
                    "min_length": "用户名不能少于两个字符",
                },
            }
        }

    re_password = serializers.CharField()

    def validate(self, attrs):
        if attrs.get("password") != attrs.pop("re_password"):
            raise exceptions.ValidationError("密码不一样")
        if not attrs.get('user_name'):
            raise exceptions.ValidationError('未输入用户名')
        user_obj = User.objects.filter(user_name=attrs.get('user_name'))
        if user_obj:
            raise exceptions.ValidationError('用户名已存在')
        return attrs
