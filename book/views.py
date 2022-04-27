from django.shortcuts import render, get_object_or_404, redirect, reverse
from . import models, forms


def book_all(request):
    book = models.Book.objects.all()
    return render(request, "book_list.html", {"book": book})


def book_show(request):
    show_book = models.BookShow.objects.all()
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

