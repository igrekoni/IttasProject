from django.shortcuts import render

from mainpage import utils


def mainpage(request):
    delta = utils.counterHelper()
    newTime = delta[0]
    newMonth = delta[1]
    newDay = delta[2]
    return render(request, "base.html", {'newTime': newTime, 'newMonth': newMonth, 'newDay': newDay})


def contacts(request):

    return render(request, "pages/contacts.html", {})


def scna(request):

    return render(request, "pages/scna.html", {})


def cna(request):

    return render(request, "pages/cna.html", {})


def dkey(request):

    return render(request, "pages/dkey.html", {})


def attestation(request):

    return render(request, "pages/attestation.html", {})


def sertification(request):

    return render(request, "pages/sertification.html", {})


def ekspertiza(request):

    return render(request, "pages/ekspertiza.html", {})


def oblast(request):

    return render(request, "pages/oblast-akkreditacii.html", {})
