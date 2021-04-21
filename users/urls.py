from django.urls import path, include

from users.views import register, activate

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
