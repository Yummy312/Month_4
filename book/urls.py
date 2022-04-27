from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('books/', views.book_all, name='book_all'),
    path('catalog/fantastic/', views.show_genre_fantastic, name="catalog_fantastic"),
    path('catalog/romantic/', views.show_genre_romantic, name="catalog_romantic"),
    path('catalog/horror/', views.show_genre_horror, name="catalog_horror"),
    path('catalog/latest/', views.latest_date, name="catalog_latest"),
    path('catalog/', views.book_show, name="book_show"),
    path('catalog/<int:id>/', views.show_detail, name="show_detail"),
    path('catalog/<int:id>/update/', views.update_book, name='catalog_update'),
    path('catalog/<int:id>/delete/', views.book_delete, name='catalog_delete'),
    path('add-book/', views.add_book, name='add_book'),


]

