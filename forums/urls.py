from django.urls import path
from .import views


app_name = 'forums'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('topic/<int:topic_id>/comment/', views.new_comment, name='new_comment'),
    path('rules/', views.rules, name='rules'),
]