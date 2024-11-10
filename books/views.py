from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated


class BookList(APIView): 
    permission_classes = [IsAuthenticated]
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class BookDetail(APIView):

    def get(self, request):
        book =  get_object_or_404(Book, pk=id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
        
    def put(self, request):
        serializer = BookSerializer(Book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, requset, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


