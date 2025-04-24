from django.db import models
from django.core.exceptions import ValidationError

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    publisher = models.ManyToManyField(Publisher, blank=True)
    summary = models.TextField(blank=True)

    def clean(self):
        if self.price is not None and self.price <= 0:
            raise ValidationError("Price must be greater than 0.")

    def save(self, *args, **kwargs):
        self.clean()  # Call the clean method to validate before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_authors')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='book_authors')

    def __str__(self):
        return f"{self.author.name} - {self.book.name}"