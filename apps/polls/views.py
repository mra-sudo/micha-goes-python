from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Poll, Choice
import json


def index(request):
    context = {'umfragen':Poll.objects.all(), 'titel':'Umfrageseite'}
    return render(request=request, template_name='polls/index.html', context=context)


def umfrage_detail(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)

    user_can_vote = True
    if 'voted_polls' in request.session:
        if type(request.session['voted_polls']) == list:
            if umfrage.id in request.session['voted_polls']:
                user_can_vote = False
    context = {'umfrage':umfrage, 'access': user_can_vote}
    return render(request=request, template_name='polls/umfrage.html', context=context)


def umfrage_vote(request, slug):
    umfrage = get_object_or_404(Poll, slug=slug)
    try:
        ausgewaelte_antwort = umfrage.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "Fehler: keine bzw. eine ungültige Antwort ausgewählt.")
        return HttpResponseRedirect(reverse('polls:umfrage-detail', args=(umfrage.slug,)))
        #return render(request=request, template_name='polls/vote.html')
    else:
        ausgewaelte_antwort.votes += 1
        ausgewaelte_antwort.save()

        if 'voted_polls' in request.session:
            if type(request.session['voted_polls']) == list:
                voted_polls = request.session['voted_polls']
                voted_polls.append(umfrage.id)
                request.session['voted_polls'] = voted_polls
            else:
                request.session['voted_polls'] = [umfrage.id]
        else:
            request.session['voted_polls'] = [umfrage.id]
        return HttpResponseRedirect(reverse('polls:umfrage-results', args=(umfrage.slug,)))


def umfrage_results(request, slug):
    results = get_object_or_404(Poll, slug=slug)
    session = len(request.session['voted_polls'])
    context = {'results':results, 'session':session}
    return render(request=request, template_name='polls/results.html', context=context)


def lat_ajax(request, slug):

    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        return HttpResponse(json.dumps(name), content_type='application/json')
        #return HttpResponse(name)

        #return HttpResponse(json.dumps({'name': name}), content_type="application/json")
        #return JsonResponse(json.dumps({'name': name}), content_type="application/json")
        #return JsonResponse({'name': name}, status=200)
    else:
        return render('polls/umfrage.html', locals())

# def postFriend(request):
#     # request should be ajax and method should be POST.
#     if request.is_ajax and request.method == "POST":
#         # get the form data
#         form = FriendForm(request.POST)
#         # save the data and after fetch the object in instance
#         if form.is_valid():
#             instance = form.save()
#             # serialize in new friend object in json
#             ser_instance = serializers.serialize('json', [instance, ])
#             # send to client side.
#             return JsonResponse({"instance": ser_instance}, status=200)
#         else:
#             # some form errors occured.
#             return JsonResponse({"error": form.errors}, status=400)
#
#     # some error occured
#     return JsonResponse({"error": ""}, status=400)
