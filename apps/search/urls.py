from django.urls import path
from .views import umfrage_suche

app_name = 'search'
urlpatterns = [
    # wenn eine Anfrage an / reinkommt, dann übergebe das der Funkt. Index aus der views.py
    path('', umfrage_suche, name='umfrage-suche'),
]