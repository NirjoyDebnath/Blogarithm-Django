from django.urls import path
from . import views
urlpatterns = [
    path('', views.CreateStory.as_view()),
    path('<uuid:pk>/', views.StoryUpdateDelete.as_view())
]