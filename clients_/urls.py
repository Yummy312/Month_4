from django.urls import path
from . import views, models

app_name = 'clients_'
urlpatterns = [
    path("registr/", views.Register.as_view(), name="registr"),
    path("login/", views.Login.as_view(), name="login"),
    path("clients/", views.ClientList.as_view(), name="clients")

    ]