from django.urls import path
from logs import views

app_name = "logs"

urlpatterns = [
    path('', views.index),
    path('topics/', views.topics,name="topics"),
    path('new_topic/', views.new_topic, name="new_topic"),
]