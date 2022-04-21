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


class BookShow(models.Model):
    GENRE_CHOICE = (
        ("Comedy", "COMEDY"),
        ("Romantic", "ROMANTIC"),
        ("Horror", "Horror"),
        ("Fantastic", "FANTASTIC")
    )
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to="")
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE)
    year_of_issue = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class BookFeedBack(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    shows = models.ForeignKey(BookShow,
                              on_delete=models.CASCADE,
                              related_name="BookFeedBack")

    def __str__(self):
        return self.shows.title