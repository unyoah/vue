from django.contrib import admin

# Register your models here.
from book.models import *

admin.site.register(Book)
admin.site.register(Press)
admin.site.register(Author)
admin.site.register(AuthorDetail)
