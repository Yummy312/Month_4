
from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=180)
    image = models.CharField(max_length=180)
    url = models.CharField(max_length=180)

    def __str__(self):
        return self.title
