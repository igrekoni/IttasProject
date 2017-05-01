from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import Post
from .forms import PostForm


def news_create(request):
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Запись успешно добавлена")
        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     messages.error(request, "Запись не создана. Проверьте логи.")
    context = {
        "form": form,
    }
    return render(request, "news/form_post.html", context)


def news_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "news/single_post.html", context)


def news_list(request):
    queryset_list = Post.objects.all() #.order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "title": "News",
        "news_list": queryset,
        "page_request_var": page_request_var,
    }
    return render(request, "news/news_list.html", context)


def news_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Запись успешно обновлена")
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "news/form_post.html", context)


def news_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Запись удалена")
    return redirect("news:list")

