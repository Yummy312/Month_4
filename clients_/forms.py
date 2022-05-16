
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Client


class RegisterForm(UserCreationForm):
    gender_types = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
        ("OTHER", "Other")
    )
    birth_date = (
        ("1990", "1990"),
        ("1991", "1991"),
        ("1992", "1992"),
        ("1993", "1993"),
        ("1994", "1994"),
        ("1995", "1995"),
        ("1996", "1996"),
        ("1997", "1997"),
        ("1998", "1998"),
        ("1999", "1999"),
        ("2000", "2000"),

    )
    country_type = (
        ("RUSSIA", "Russia"),
        ("KAZAKHSTAN", "Kazakhstan"),
        ("KYRGYZSTAN", "Kyrgyzstan"),
        ("UZBEKISTAN", "Uzbekistan")
    )
    gender = forms.ChoiceField(choices=gender_types, required=True)
    birth = forms.ChoiceField(choices=birth_date, required=True)
    email = forms.EmailField(required=True)
    address = forms.CharField(required=True)
    phone_number = forms.CharField(max_length=100)
    favorite_word = forms.CharField(max_length=25)
    favorite_number = forms.CharField(max_length=30)
    country = forms.ChoiceField(choices=country_type, required=True)

    class Meta:
        model = Client
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "gender",
            "birth",
            "address",
            "favorite_word",
            "favorite_number",
            "country",
            "phone_number"
        ]

    def save(self, commit=True):
        client = super(RegisterForm, self).save(commit=False)
        client.email = self.cleaned_data["email"]
        if commit:
            client.save()
        return client


class LoginForm(AuthenticationForm):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "email ",
                "id": "email"
            }
        )
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "phone_number",
                "id": " phone_number"
            }
        )
    )

    password = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "password",
                "id": "password"
            }
        )
    )

