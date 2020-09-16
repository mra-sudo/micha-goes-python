from django.urls import path
from .views import index, umfrage_detail, umfrage_vote, umfrage_results, lat_ajax

app_name = 'polls'
urlpatterns = [
    # wenn eine Anfrage an / reinkommt, dann übergebe das der Funkt. Index aus der views.py
    path('', index, name='index'),
    path('<str:slug>/', umfrage_detail, name='umfrage-detail'),
    path('<str:slug>/vote/', umfrage_vote, name='umfrage-vote'),
    path('<str:slug>/results/', umfrage_results, name='umfrage-results'),
    path('<str:slug>/post/ajax/', lat_ajax, name='lat-ajax'),
]