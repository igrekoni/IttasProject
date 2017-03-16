from django.shortcuts import render


def mainpage(request):

    return render(request, "base.html", {})


def contacts(request):

    return render(request, "contacts.html", {})
