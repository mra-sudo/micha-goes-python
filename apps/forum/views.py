from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.urls import reverse
from .models import Topic, Post
from django.core import serializers
from .forms import CreateTopic
from django.utils import timezone



def index(request):
    context = {'topics':Topic.objects.all()}
    return render(request=request, template_name='forum/index.html', context=context)


def topic_detail(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    context = {'topic':topic}
    return render(request=request, template_name='forum/topic.html', context=context)

def create_topic(request):
    form = CreateTopic()
    #topics = Topic.objects.all()
    #context = {"form": form, "topics": Topic}
    context = {"form": form}
    return render(request=request, template_name='forum/create.html', context=context)
    #return render(request=request, template_name='forum/create.html')


def post_new(request):
    if request.method == "POST":
        form = CreateTopic(request.POST)
        context = {"form": form}
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_time = timezone.now()
            post.save()
            #return redirect('topic_detail', slug=post.slug)
            return redirect('topic_detail')
            #return reverse('topic_detail', slug=post.slug)
            #return HttpResponseRedirect('topic_detail', slug=post.slug)
        else:
            return render(request=request, template_name='forum/create.html', context=context)
    else:
        form = CreateTopic()
        context = {"form": form}
        return render(request=request, template_name='forum/create.html', context=context)
    #return render(request, 'forum/create.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Topic, slug=slug)
    if request.method == "POST":
        form = CreateTopic(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_time = timezone.now()
            post.save()
            return redirect('topic_detail', slug=post.slug)
    else:
        form = CreateTopic(instance=post)
    return render(request, 'forum/create.html', {'form': form})
#
#
#     if request.method == "POST":
#         form = CreateTopic(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.publish_time = timezone.now()
#             post.save()
#             return redirect('topic_detail', slug=post.slug)
#     else:
#         form = CreateTopic()
#         context = {"form": form}
#     return render(request=request, template_name='forum/create.html', context=context)


# def edit_topic(request, slug):
#     post = get_object_or_404(Topic, slug=slug)
#     if request.method == "POST":
#         form = CreateTopic(request.POST, instance=post)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.publish_time = timezone.now()
#             post.save()
#             return redirect('topic_detail', slug=post.slug)
#     else:
#         form = CreateTopic(instance=post)
#         context = {"form": form}
#     return render(request=request, template_name='forum/create.html', context=context)


# def ajax_create_topic(request):
#     # request should be ajax and method should be POST.
#     if request.is_ajax and request.method == "POST":
#         # get the form data
#         form = CreateTopic(request.POST)
#         # save the data and after fetch the object in instance
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.author = request.user
#             instance.publish_time = timezone.now()
#             instance.save()
#             # serialize in new topic object in json
#             ser_instance = serializers.serialize('json', [instance, ])
#             # send to client side.
#             return JsonResponse({"instance": ser_instance}, status=200)
#         else:
#             # some form errors occured.
#             return JsonResponse({"error": form.errors}, status=400)
#
#     # some error occured
#     return JsonResponse({"error": ""}, status=400)

    #return render(request=request, template_name='forum/topic.html', context=context)
