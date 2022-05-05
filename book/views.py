from django.shortcuts import get_object_or_404
from . import models, forms
from django.views import generic


class Booklist(generic.ListView):
    template_name = "show_books.html"
    queryset = models.BookShow.objects.order_by("-id")

    def get_queryset(self):
        return self.queryset


class BookDetail(generic.DetailView):
    template_name = "details.html"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.BookShow, id=book_id)


class BookAdd(generic.CreateView):
    template_name = "add_books.html"
    form_class = forms.BookForm
    queryset = models.BookShow.objects.all()
    success_url = '/catalog/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookAdd, self).form_valid(form=form)


class BookUpdate(generic.UpdateView):
    template_name = "book_update.html"
    form_class = forms.BookForm
    success_url = "/catalog/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.BookShow, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookUpdate, self).form_valid(form=form)


class BookDelete(generic.DeleteView):
    success_url = "/catalog"
    template_name = "delete_book.html"

    def get_object(self, *kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.BookShow, id=book_id)


#
# def book_delete(request, id):
#     book_id = get_object_or_404(models.BookShow, id=id)
#     book_id.delete()
#     return redirect(reverse("book:book_show"))


# def update_book(request, id):
#     book_id = get_object_or_404(models.BookShow, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(instance=book_id,
#                               data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('book:book_show'))
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(request, "book_update.html", {"form": form,
#                                                 "detail": book_id})
#
# def book_delete_(request, id):
#     book_id = get_object_or_404(models.BookShow, id=id)
#     book_id.delete()
#     return redirect(reverse("book:book_show"))
