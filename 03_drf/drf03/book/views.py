from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer
from rest_framework.mixins import *
from book.models import Book


class BookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            book = Book.objects.get(pk=book_id)
            data = BookSerializer(book).data
            return Response({
                'status': 200,
                'msg': '查询单个成功',
                'results': data
            })
        else:
            book = Book.objects.all()
            print(book)
            data = BookSerializer(book, many=True).data
            return Response({
                'status': 200,
                'msg': '查询多个成功',
                'results': data
            })

    def post(self, request, *args, **kwargs):
        request_data = request.data

        if isinstance(request_data, dict):
            many = False
        elif isinstance(request_data, list):
            many = True
        else:
            return Response({
                'status': 400,
                'msg': '添加错误',
            })
        books = BookSerializer(data=request_data, many=many)
        books.is_valid(raise_exception=True)
        books = books.save()
        return Response({
            'status': 200,
            'msg': '添加成功',
            'results': BookSerializer(books, many=many).data
        })

    def delete(self, request, *args, **kwargs):
        book_id = kwargs.get('id')
        if book_id:
            ids = [book_id]
        else:
            ids = request.data.get('ids')
        res = Book.objects.filter(pk__in=ids, is_delete=False).update(is_delete=True)
        print(res)
        if res:
            return Response({
                'status': 200,
                'msg': '删除成功',
            })
        return Response({
            'status': 400,
            'msg': '删除失败',
        })

    def put(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get('id')
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'status': 400,
                'msg': '修改失败',
            })
        serializer = BookSerializer(data=request_data, instance=book)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': 200,
            'msg': '修改成功',
            'results': BookSerializer(book).data
        })

    def patch(self, request, *args, **kwargs):
        request_data = request.data
        book_id = kwargs.get('id')
        # try:
        #     book = Book.objects.get(pk=book_id)
        # except Book.DoesNotExist:
        #     return Response({
        #         'status': 400,
        #         'msg': '修改失败',
        #     })
        # serializer = BookSerializer(data=request_data, instance=book, partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response({
        #     'status': 200,
        #     'msg': '修改成功',
        #     'results': BookSerializer(book).data
        # })

        if book_id and isinstance(request_data, dict):
            book_ids = [book_id]
            request_data = [request_data]
        elif not book_id and isinstance(request_data, list):
            book_ids = []
            for dic in request_data:
                pk = dic.pop('id', None)
                if pk:
                    book_ids.append(pk)
                else:
                    return Response({
                        'status': status.HTTP_400_BAD_REQUEST,
                        'message': 'PK不存在'
                    })
        else:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': '参数格式不正确'
            })
        book_list = []
        new_data = []
        for index, pk in enumerate(book_ids):
            try:
                book_objects = Book.objects.get(pk=pk)
                book_list.append(book_objects)
                new_data.append(request_data[index])
            except Book.DoesNotExist:
                continue
        book_serializer = BookSerializer(data=new_data, instance=book_list, partial=True, many=True)
        book_serializer.is_valid(raise_exception=True)
        book_serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'message': '修改成功'
        })


class BookGenericAPIView(GenericAPIView, RetrieveModelMixin, ListModelMixin
    , DestroyModelMixin, CreateModelMixin, UpdateModelMixin):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        if 'id' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # return self.update(request, *args, **kwargs)
        return self.partial_update(request, *args, **kwargs)


class BookGenericsAPIView(generics.RetrieveUpdateDestroyAPIView, generics.CreateAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer
    lookup_field = 'id'
