from django.shortcuts import render

def index(request):
    test = False
    if request.session.has_key('loggedin'):
        test = True
    context = {'login':test}
    return render(request=request, template_name='index/index.html', context=context)