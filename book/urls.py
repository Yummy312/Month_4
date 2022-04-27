from django.urls import path
from . import views
app_name = 'book'
urlpatterns = [
    path('books/', views.book_all, name='book_all'),
    path('catalog/', views.book_show, name="book_show"),
    path('catalog/<int:id>/', views.show_detail, name="show_detail"),
    path('add-book/', views.add_book, name='add_book')

]

