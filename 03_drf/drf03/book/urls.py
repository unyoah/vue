from django.urls import path
from book.views import BookAPIView, BookGenericAPIView, BookGenericsAPIView

urlpatterns = [
    path('book/', BookAPIView.as_view()),
    path('book/<str:id>/', BookAPIView.as_view()),
    path('gen/book/', BookGenericAPIView.as_view()),
    path('gen/book/<str:id>/', BookGenericAPIView.as_view()),
    path('gens/book/', BookGenericsAPIView.as_view()),
    path('gens/book/<str:id>/', BookGenericsAPIView.as_view())
]
