from rest_framework import serializers

from books.serializers import BookSerializer
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    book_title = serializers.SerializerMethodField()  # Add a custom field for title

    class Meta:
        model = Review
        fields = ['id', 'book_title', 'content']  # Replace 'book' with 'book_title' if you only need the title

    def get_book_title(self, obj):
        return obj.book.title