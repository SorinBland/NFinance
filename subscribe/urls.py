from django.urls import path

from subscribe.views import subscribe, subscribe_mails, unsubscribe

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('subscribe-email/', subscribe_mails, name='subscribe_mails'),
    path("unsubscribe/", unsubscribe, name="unsubscribe"),

]