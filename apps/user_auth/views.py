from django.shortcuts import render
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def login(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        # A backend authenticated the credentials
        loggedin = True
        request.session['loggedin'] = loggedin
        context = {'user':user}
        return render(request=request, template_name='user_auth/intern.html', context=context)
    else:
        # No backend authenticated the credentials
        return render(request=request, template_name='user_auth/login.html')


def internView(request):
    if request.session.has_key('loggedin'):
        #username = request.session['username']
        return render(request=request, template_name='user_auth/intern.html')
    else:
        return render(request=request, template_name='user_auth/login.html')


def logout(request):
   try:
      del request.session['loggedin']
      messages.info(request, "Erfolgreich ausgeloggt.")
   except:
      pass
   return HttpResponseRedirect(reverse('index:index'))