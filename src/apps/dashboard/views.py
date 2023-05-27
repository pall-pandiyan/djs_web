from django.shortcuts import render, redirect


def home(request):
    return render(
        request=request,
        template_name="dashboard/home.html",
        context={}
    )
