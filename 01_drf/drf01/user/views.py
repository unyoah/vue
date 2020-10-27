from django.http import JsonResponse, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.views import APIView
from user.models import User


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            user = User.objects.filter(pk=id).values('user_name', 'password', 'gender').first()
            if user:
                return JsonResponse({
                    'status': 200,
                    'msg': '单个查询',
                    'result': user
                })
        else:
            user_objects_all = User.objects.all().values('user_name', 'password', 'gender')
            if user_objects_all:
                return JsonResponse({
                    'status': 200,
                    'msg': '查询所有',
                    'result': list(user_objects_all)
                })
        return JsonResponse({
            'status': 400,
            'msg': '失败',

        })

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create(user_name=user_name, password=password)
            return JsonResponse({
                'status': 200,
                'msg': '添加成功',
                'result': {'user_name': user.user_name, 'password': user.password}
            })
        except:
            return JsonResponse({
                'status': 400,
                'msg': '添加失败',
            })

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            User.objects.get(pk=id).delete()
            return JsonResponse({
                'status': 200,
                'msg': '删除成功',

            })
        except:
            return JsonResponse({
                'status': 400,
                'msg': '删除失败',
            })


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id:
            user = User.objects.filter(pk=id).values('user_name', 'password', 'gender').first()
            if user:
                return Response({
                    'status': 200,
                    'msg': '单个查询',
                    'result': user
                })
        else:
            user_objects_all = User.objects.all().values('user_name', 'password', 'gender')
            if user_objects_all:
                return Response({
                    'status': 200,
                    'msg': '查询所有',
                    'result': list(user_objects_all)
                })
        return Response({
            'status': 400,
            'msg': '失败',

        })

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.create(user_name=user_name, password=password)
            return Response({
                'status': 200,
                'msg': '添加成功',
                'result': {'user_name': user.user_name, 'password': user.password}
            })
        except:
            return Response({
                'status': 400,
                'msg': '添加失败',
            })

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('id')
        try:
            User.objects.get(pk=id).delete()
            return Response({
                'status': 200,
                'msg': '删除成功',

            })
        except:
            return Response({
                'status': 400,
                'msg': '删除失败',
            })
