from django.urls import path

from subscribe.views import subscribe, subscribe_mails

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('subscribe-email/', subscribe_mails, name='subscribe_mails'),
]