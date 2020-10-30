from rest_framework.response import Response
from rest_framework.views import APIView
from book.serializers import BookSerializer

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
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            return Response({
                'status': 400,
                'msg': '修改失败',
            })
        serializer = BookSerializer(data=request_data, instance=book, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'status': 200,
            'msg': '修改成功',
            'results': BookSerializer(book).data
        })
