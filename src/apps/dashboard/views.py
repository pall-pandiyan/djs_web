from django.shortcuts import render, redirect


def home(request):
    """
    View to show the main dashboard page.
    
    Developer: Pall Pandiyan.S
    """
    return render(
        request=request,
        template_name="dashboard/home.html",
        context={}
    )
