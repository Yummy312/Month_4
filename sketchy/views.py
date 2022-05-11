from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from . import models, forms


class ViewFormParse(generic.FormView):
    template_name = "parser.html"
    form_class = forms.ParserContainer

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parse_data()
            # return HttpResponse("Parse data success")
            return redirect(reverse("sketchy:content_view"))
        else:
            return super(ViewFormParse, self).post(request, *args, **kwargs)


class ContentView(generic.ListView):
    template_name = "content.html"
    queryset = models.Content.objects.all()

    def get_queryset(self):
        return self.queryset