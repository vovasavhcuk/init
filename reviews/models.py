from django.db import models

from books.models import Book

# Create your models here.
class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return f"<Book(id={self.book.id}, title={self.book.title}, author={self.book.author}, review={self.content}>"


