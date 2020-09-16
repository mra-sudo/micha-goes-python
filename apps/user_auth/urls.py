from django.urls import path
from .views import login, internView, logout

app_name = 'user_auth'
urlpatterns = [
    # wenn eine Anfrage an / reinkommt, dann übergebe das der Funkt. Index aus der views.py
    path('', internView, name='internView'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]