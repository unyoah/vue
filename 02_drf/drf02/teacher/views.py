from rest_framework.response import Response
from rest_framework.views import APIView

from teacher.models import Teacher
from teacher.serializers import TeacherSerializer, TeacherDeSerializer


class TeacherAIPView(APIView):
    def get(self, request, *args, **kwargs):
        teacher_id = kwargs.get('id')
        if teacher_id:
            teacher_objects = Teacher.objects.get(pk=teacher_id)
            serializer = TeacherSerializer(teacher_objects).data
            return Response({
                'status': 200,
                'msg': '查询单个教师信息',
                'results': serializer
            })
        teacher_objects_all = Teacher.objects.all()
        teacher_serializer = TeacherSerializer(teacher_objects_all, many=True).data
        return Response({
            'status': 200,
            'msg': '查询多个教师信息',
            'results': teacher_serializer
        })

    def post(self, request, *args, **kwargs):
        request_data = request.data

        if not isinstance(request_data, dict) or request_data == {}:
            return Response({
                'status': 400,
                'msg': '添加失败',
            })
        teacher_de_serializer = TeacherDeSerializer(data=request_data)
        if teacher_de_serializer.is_valid():
            de_serializer_save = teacher_de_serializer.save()
            return Response({
                'status': 200,
                'msg': '添加成功',
                'results': request_data
            })

    def delete(self, request, *args, **kwargs):
        teacher_id = kwargs.get('id')
        print(teacher_id)
        teacher = Teacher.objects.filter(pk=teacher_id)[0]
        print(teacher)
        if teacher:
            teacher_delete = teacher.delete()
            print(teacher_delete)
            return Response({
                'status': 200,
                'msg': '删除成功',
            })
        return Response({
            'status': 400,
            'msg': '删除失败',

        })
