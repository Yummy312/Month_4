from django.test import TestCase
from unittest import TestCase
from . import models, parser


class TestModel(TestCase):

    def test_model_Content_create_success(self):
        temp = {
            "title": "Test title",
            "image": "Test image",
            "url": " Test url"
        }
        content = models.Content.objects.create(**temp)
        self.assertEqual(content.title, temp['title'])

    def test_model_Content__create_fail(self):
        temp = {
            "title": "Test title",
            "image": "Test image",
            "url": 122
        }

        with self.assertRaises(ValueError):
            content = models.Content.objects.create(**temp)
            raise ValueError("You need to enter the other values.")

    def test_model_Content__update(self):
        temp = {
            "title": "Test title",
            "image": "Test image",
            "url": " Test url"
        }
        new_url = "URL"
        content = models.Content.objects.create(**temp)
        content.url = new_url
        content.save()
        content.refresh_from_db()
        print(content.url)

    def test_model_Content__delete(self):
        temp = {
            "title": "Test title",
            "image": "Test image",
            "url": " Test url"
        }
        content = models.Content.objects.create(**temp)
        pk = content.pk
        print(pk)
        content.delete()
        with self.assertRaises(models.Content.DoesNotExist):
            models.Content.objects.get(pk=pk)


class TestParser(TestCase):
    def test_parser_function(self):
        with self.assertRaises(TypeError):
            data = parser.parser_func(-1)
            raise TypeError('parser_func() takes 0 positional arguments but 1 was given')
        with self.assertRaises(AttributeError):
            data = parser.get_htm()
            raise AttributeError("The module has no attribute")


