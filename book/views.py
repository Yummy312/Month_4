from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms
from datetime import datetime, timedelta

date = datetime.today() - timedelta(days=2)


def book_all(request):
    book = models.Book.objects.all()
    return render(request, "book_list.html", {"book": book})


def book_show(request):
    show_book = models.BookShow.objects.filter().order_by("-id")
    return render(request, "show_books.html", {"show_book": show_book})


def show_detail(request, id):
    detail = get_object_or_404(models.BookShow, id=id)
    return render(request, "details.html", {"detail": detail})


def add_book(request):
    method = request.method
    if method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('book:book_show'))
    else:
        form = forms.BookForm()
    return render(request, "add_books.html", {'form': form})


def book_delete(request, id):
    book_id = get_object_or_404(models.BookShow, id=id)
    book_id.delete()
    return redirect(reverse("book:book_show"))


def update_book(request, id):
    book_id = get_object_or_404(models.BookShow, id=id)
    if request.method == 'POST':
        form = forms.BookForm(instance=book_id,
                              data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('book:book_show'))
    else:
        form = forms.BookForm(instance=book_id)
    return render(request, "book_update.html", {"form": form,
                                                "detail": book_id})


def latest_date(request):
    show_book = models.BookShow.objects.filter(created_date__gt=date).order_by("-id")
    return render(request, "show_books.html", {"show_book": show_book})


def show_genre_horror(request):
    show_book = models.BookShow.objects.filter(genre="Horror")
    return render(request, "show_books.html", {"show_book": show_book})


def show_genre_romantic(request):
    show_book = models.BookShow.objects.filter(genre="Romantic")
    return render(request, "show_books.html", {"show_book": show_book})


def show_genre_fantastic(request):
    show_book = models.BookShow.objects.filter(genre="Fantastic")
    return render(request, "show_books.html", {"show_book": show_book})


def book_delete_(request, id):
    book_id = get_object_or_404(models.BookShow, id=id)
    book_id.delete()
    return redirect(reverse("book:book_show"))
