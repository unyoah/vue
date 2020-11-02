from django.urls import path

from users import views

urlpatterns = [
    path('login/', views.UserView.as_view({'post': 'user_login'})),
    path('register/', views.UserView.as_view({'post': 'user_register'})),
]
