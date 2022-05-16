
from django.db import models
from django.contrib.auth.models import User


class Client(User):
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

    gender = models.CharField(choices=gender_types, max_length=80)
    birth = models.CharField(choices=birth_date, max_length=30)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    favorite_word = models.CharField(max_length=25, null= True)
    favorite_number = models.CharField(max_length=30, null=True)
    country = models.CharField(choices=country_type, max_length=30, null=True)
