from django.urls import path

from teacher import views

urlpatterns = [
    path('teacher/', views.TeacherAIPView.as_view()),
    path('teacher/<id>/', views.TeacherAIPView.as_view())
]
