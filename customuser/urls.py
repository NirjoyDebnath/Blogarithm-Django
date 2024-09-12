from django.urls import path
from . import views
urlpatterns = [
    path('signup/', views.sign_up),
    path('login/', views.log_in),
    path('logout/', views.log_out),
    path('', views.UserList.as_view()),
    path('<uuid:pk>/', views.User.as_view())
]