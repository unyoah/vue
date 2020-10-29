from django.urls import path
from book.views import BookAPIView

urlpatterns = [
    path('book/', BookAPIView.as_view()),
    path('book/<str:id>/', BookAPIView.as_view())
]
