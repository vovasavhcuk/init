from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    author = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return f"<Book(id={self.id}, title={self.title}, author={self.author}>"
