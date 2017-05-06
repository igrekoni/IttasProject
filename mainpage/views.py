from django.core.mail import send_mail
from django.http import BadHeaderError
from django.shortcuts import render, HttpResponse
from mainpage import utils
from mainpage.forms import FeedbackForm


def mainpage(request):
    delta = utils.counterHelper()
    newTime = delta[0]
    newMonth = delta[1]
    newDay = delta[2]
    return render(request, "base.html", {'newTime': newTime, 'newMonth': newMonth, 'newDay': newDay})


def contacts(request):
    if request.method == 'POST':
        feedback = FeedbackForm(request.POST)
        if feedback.is_valid():
            subject = feedback.cleaned_data['customer_name']
            from_email = feedback.cleaned_data['email']
            message = feedback.cleaned_data['form_message']
            feedback.save()
            try:
                send_mail(subject, message, from_email, ['grechkoia@solit.by'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return render(request, 'base.html')
    else:
        feedback = FeedbackForm()

    return render(request, "pages/contacts.html", {'form': feedback})


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


def audit(request):

    return render(request, "pages/audit.html", {})


def soprovozhdenie(request):

    return render(request, "pages/soprovozhdenie-po.html", {})


def razrabotka(request):

    return render(request, "pages/razrabotka-po.html", {})


def company(request):

    return render(request, "pages/o-kompanii.html", {})


def vacancies(request):

    return render(request, "pages/vacancies.html", {})
