from django.test import TestCase
from .models import Author, Book


class ModelTests(TestCase):
    def setUp(self):
        self.author = Author.objects.create(
            first_name="John", last_name="Doe", birth_date="1980-01-01"
        )
        self.book = Book.objects.create(
            title="Test Book", publication_date="1800-06-06", author=self.author
        )

    def test_author_str(self):
        self.assertEqual(str(self.author), "John Doe")

    def test_book_str(self):
        self.assertEqual(str(self.book), "Test Book")
