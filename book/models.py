from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=40)
    description = models.TextField()
    crate_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now =True)
    image = models.ImageField(upload_to='')

    def __str__(self):
        return self.title