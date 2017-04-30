from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from news.models import Post
from .forms import PostForm


def news_create(request):
    form = PostForm(request.POST or None)
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
    return render(request, "news_templates/form_post.html", context)


def news_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "news_templates/single_post.html", context)


def news_list(request):
    queryset = Post.objects.all()
    context = {
        "title": "News",
        "news_list": queryset,
    }
    return render(request, "news_templates/news.html", context)


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
    return render(request, "news_templates/form_post.html", context)


def news_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Запись удалена")
    return redirect("news:list")

