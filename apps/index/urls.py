from django.urls import path
from .views import index

app_name = 'index'
urlpatterns = [
    # wenn eine Anfrage an / reinkommt, dann übergebe das der Funkt. Index aus der views.py
    path('', index, name='index'),
]