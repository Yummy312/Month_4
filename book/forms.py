from django import forms
from . import models


class BookForm(forms.ModelForm):
    class Meta:
        model = models.BookShow
        fields = "__all__"
