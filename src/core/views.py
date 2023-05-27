from django.http import HttpResponse
from django.shortcuts import render, redirect


def index(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return redirect("dashboard:home")
        return redirect("dashboard:home")

    return redirect("accounts:login")
