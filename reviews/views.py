from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Review

from reviews.serializers import ReviewSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ReviewList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
class ReviewDetail(APIView):

    def get(self, request):
        review =  get_object_or_404(Review, pk=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
        
    def put(self, request):
        serializer = ReviewSerializer(Review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, requset, id):
        review = Review.objects.get(pk=id)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)