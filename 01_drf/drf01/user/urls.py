from django.urls import path
from user import views

urlpatterns = [
    path('user/<str:id>/', views.UserView.as_view()),
    path('user/', views.UserView.as_view()),
    path('useraip/<str:id>/', views.UserAPIView.as_view()),
    path('useraip/', views.UserAPIView.as_view()),
]
