from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # A backend authenticated the credentials
        context = {'user': user}
        auth_login(request, user)
        return render(request=request, template_name='user_auth/intern.html', context=context)
    else:
        # No backend authenticated the credentials
        return render(request=request, template_name='user_auth/login.html')


def internView(request):
    if request.user.is_authenticated:
        return render(request=request, template_name='user_auth/intern.html')
    else:
        return render(request=request, template_name='user_auth/login.html')


def logout(request):
   try:
      auth_logout(request)
      messages.info(request, "Erfolgreich ausgeloggt.")
   except:
      pass
   return HttpResponseRedirect(reverse('index:index'))