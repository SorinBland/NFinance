from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse

from users.forms import CustomUserCreationForm


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(
                request, "login.html",
            )
    else:
        form = CustomUserCreationForm()
    args = {'form': form}
    return render(
        request, "registration/users.html", args
    )
