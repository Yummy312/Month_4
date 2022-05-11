from django.urls import path
from . import views, models

app_name = 'sketchy'
urlpatterns = [

    path('parse/', views.ViewFormParse.as_view(), name="parse_view"),
    path('content/', views.ContentView.as_view(queryset= models.Content.objects.order_by("-id"))
                                                                                         , name="content_view")
    ]