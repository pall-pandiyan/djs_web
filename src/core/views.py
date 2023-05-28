from django.shortcuts import redirect


def index(request):
    """
    This is the starting point of our application, if the user is already logged in redirected to user's home (dashboard or admin page). Otherwiser redirect to login page.

    Developer: Pall Pandiyan.S
    """
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return redirect("admin:index")
        return redirect("dashboard:home")
    return redirect("accounts:login")
