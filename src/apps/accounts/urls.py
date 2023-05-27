from django.urls import path
from . import views

urlpatterns = [
    path('login', views.Login.as_view(), name="login"),
    path('login1', views.login_view, name="login1"),
    path('logout', views.Logout.as_view(), name="logout"),
]
