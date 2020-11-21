from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.book import Book
from ..serializers import BookSerializer

# Create your views here.
class Books(APIView):
    def get(self, request):
        """Index Request"""
        print(request)
        books = Book.objects.all()[:10]
        data = BookSerializer(books, many=True).data
        return Response(data)

    serializer_class = BookSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        book = BookSerializer(data=request.data['book'])
        if book.is_valid():
            b = book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        book = get_object_or_404(Book, pk=pk)
        ms = BookSerializer(book, data=request.data['book'], partial=True)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
