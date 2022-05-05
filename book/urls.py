from django.urls import path
from . import views, models
from datetime import datetime, timedelta
date = datetime.today() - timedelta(days=1)
app_name = 'book'
urlpatterns = [

    path('catalog/', views.Booklist.as_view(), name="catalog_all"),

    path('catalog/latest/',
         views.Booklist.as_view(queryset=models.BookShow.objects.filter(created_date__gt=date).order_by("-id")),
         name='catalog_latest'),

    path('catalog/horror/', views.Booklist.as_view(queryset=models.BookShow.objects.filter(genre="Horror").order_by("-id")),
         name='catalog_horror'),

    path('catalog/romantic/', views.Booklist.as_view(queryset=models.BookShow.objects.filter(genre="Romantic").order_by("-id")),
         name='catalog_romantic'),

    path('catalog/fantastic/',
         views.Booklist.as_view(queryset=models.BookShow.objects.filter(genre="Fantastic").order_by("-id")),
         name='catalog_fantastic'),

    path('catalog/<int:id>/', views.BookDetail.as_view(), name="catalog_detail"),

    path('add-book/', views.BookAdd.as_view(), name='add_book'),

    path('catalog/<int:id>/update/', views.BookUpdate.as_view(), name='catalog_update'),

    path('catalog/<int:id>/delete/', views.BookDelete.as_view(), name='catalog_delete'),
]

