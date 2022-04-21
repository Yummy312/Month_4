from django.shortcuts import render, get_object_or_404
from . import models


def book_all(request):
    book = models.Book.objects.all()
    return render(request, "book_list.html", {"book": book})


def book_show(request):
    show_book = models.BookShow.objects.all()
    return render(request, "show_books.html", {"show_book": show_book})


def show_detail(request, id):
    detail = get_object_or_404(models.BookShow, id=id)
    return render(request, "details.html", {"detail": detail})