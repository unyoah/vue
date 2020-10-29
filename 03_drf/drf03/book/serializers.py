from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ('book_name', 'price', 'publish', 'author', 'pic')

        extra_kwargs = {
            'book_name': {
                'required': True,
                'min_length': 2,
                'error_messages': {
                    'required': '图书名必须提供',
                    'min_length': '不得少于两个字符'
                }
            },
            'pic': {
                'read_only': True
            },
            'publish': {
                'write_only': True
            },
            'author': {
                'write_only': True
            },
        }
    def validate(self, attrs):
        print(attrs)
        return attrs
