from django.shortcuts import render
from django.contrib import messages
from apps.polls.models import Poll
from django.core.exceptions import ObjectDoesNotExist


def umfrage_suche(request):
    try:
        ergebnis = Poll.objects.filter(name__contains=request.POST['search'])
    #except Poll.DoesNotExist:
    except(KeyError, ergebnis.DoesNotExist):
        messages.error(request, "Es wurde keine Umfrage gefunden.")
        context = {'response': False, 'query':request.POST['search']}
        return render(request=request, template_name='search/search.html', context=context)
    else:
        context = {'ergebnis': ergebnis, 'response': True, 'query': request.POST['search']}
        return render(request=request, template_name='search/search.html', context=context)
