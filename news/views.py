from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from news.models import Post


def news_create(request):

    return HttpResponse("<p>create</p>")


def news_detail(request):
    instance = get_object_or_404(Post, id=1)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "pages/single_post.html", context)


def news_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "News",
        "news_list": queryset,
    }
    return render(request, "pages/news.html", context)


def news_update(request):

    return HttpResponse("<p>update</p>")


def news_delete(request):

    return HttpResponse("<p>delete</p>")

