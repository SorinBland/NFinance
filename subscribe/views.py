from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from Finance_news_aggregator.settings import EMAIL_HOST_USER
from finance_app.models import Headline
from subscribe import forms
import smtplib
from subscribe.models import SubEmails
import uuid


# Emails that are sent
def subscribe_mails():
    mail_subject = "Your news!"
    headlines = Headline.objects.all()[::-1]
    message = render_to_string('subscribe/subscribe_mail_sent.html', {'headlines': headlines[:3]})
    mails = SubEmails.objects.all()
    list_mails = []
    for mail in mails:
        if mail.email not in list_mails:
            list_mails.append(mail.email)
    email = EmailMessage(
        mail_subject, message, to=list_mails
    )
    print('Sending email')
    email.send()
    print('Email sent')


# Subscribe method + welcome message
def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST' and 'subscribe' in request.POST:
        try:
            new_mail = SubEmails()
            sub = forms.Subscribe(request.POST)
            subject = 'Welcome to NFinance!'
            message = 'We promise to not spam you! ' \
                      'You will get three time a month the most recent news!'
            to_email = str(sub['email'].value())
            new_mail.email = to_email

            if sub.is_valid():
                new_mail.uuid = uuid.uuid4()
                new_mail.save()
            send_mail(subject,
                      message, EMAIL_HOST_USER, [to_email], fail_silently=False)
            return render(request, 'subscribe/success.html', {'to_email': to_email})

        except IntegrityError:
            return render(request, 'subscribe/subscribe_already_subscribed.html', {'form': sub})

        except smtplib.SMTPRecipientsRefused:
            return render(request, 'subscribe/subscribe_mail_error.html', {'form': sub})

    return render(request, 'subscribe/subscribe.html', {'form': sub})


# Unsubscribe method
def unsubscribe(request):
    form = forms.Subscribe(request.POST)
    if form.is_valid():
        user_mail = str(form['email'].value())
        database_email = str(request.user.email)
        if user_mail == database_email:
            SubEmails.objects.filter(email=user_mail).delete()
            return render(request, "subscribe/unsubscribed.html")
        return HttpResponse("We don't recognize this email!")
    else:
        return render(request, "subscribe/unsubscribe.html", {"form": form})
