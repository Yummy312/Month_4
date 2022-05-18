from django.test import TestCase
from . import models


class TestModel(TestCase):

    def test_model_BookShow_create_success(self):
        book = {
            "title": "Test title",
            "author": "Test author",
            "description": "Test description",
            "image": "Test image",
            "created_date": "Test created_date",
            "update_date": "Test update_date",
            "genre": "Test genre",
            "year_of_issue": 122

        }
        content = models.BookShow.objects.create(**book)
        self.assertEqual(content.author, book['author'])

    def test_model_BookShow_create_fail(self):
        book = {
            "title": "Test title",
            "author": True,
            "description": "Test description",
            "image": "Test image",
            "created_date": "Test created_date",
            "update_date": "Test update_date",
            "genre": "Test genre",
            "year_of_issue": 122,
            "page": "Test Page"

        }

        with self.assertRaises(TypeError):
            content = models.BookShow.objects.create(**book)

    def test_model_BookShow__update(self):
        book = {
            "title": "Test title",
            "author": "Test author",
            "description": "Test description",
            "image": "Test image",
            "created_date": "Test created_date",
            "update_date": "Test update_date",
            "genre": "Test genre",
            "year_of_issue": 122

        }

        new_title = "TITLE"
        content = models.BookShow.objects.create(**book)
        content.title = new_title
        content.save()
        content.refresh_from_db()
        print(content.title)

    def test_model_BookShow__delete(self):
        book = {
            "title": "Test title",
            "author": "Test author",
            "description": "Test description",
            "image": "Test image",
            "created_date": "Test created_date",
            "update_date": "Test update_date",
            "genre": "Test genre",
            "year_of_issue": 122

        }
        content = models.BookShow.objects.create(**book)
        pk = content.pk
        print(pk)
        content.delete()
        with self.assertRaises(models.BookShow.DoesNotExist):
            models.BookShow.objects.get(pk=pk)
