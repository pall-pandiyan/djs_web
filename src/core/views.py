from django.http import HttpResponse

def index(request):
    user = request.user
    if user.is_authenticated:
        if user.is_superuser:
            return HttpResponse("Super User!")
        return HttpResponse("Authenticated!")
    return HttpResponse("NOT Authenticated!")
