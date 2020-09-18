from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
    # wenn eine Anfrage an / reinkommt, dann übergebe das der Funkt. Index aus der views.py
    path('', views.index, name='index'),
    path('<str:slug>/', views.topic_detail, name='topic_detail'),
    #path('topic/create/', create_topic, name='create-topic'),
    path('<str:slug>/edit/', views.topic_edit, name='topic_edit'),
    path('topic/create/', views.topic_new, name='topic_new'),
    #path('topic/create/post/ajax/', ajax_create_topic, name='ajax-create-topic'),
]