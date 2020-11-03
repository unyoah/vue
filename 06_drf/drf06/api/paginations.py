from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.pagination import CursorPagination


class MyPageNumberPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 5
    page_size_query_param = "page_size"
    page_query_param = "page"


class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 5


class MyCursorPagination(CursorPagination):
    cursor_query_param = "course"
    page_size = 1
    page_size_query_param = "page_size"
    max_page_size = 5
    ordering = "price"
