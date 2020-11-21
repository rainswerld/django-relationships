from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.author import Author
from ..serializers import AuthorSerializer

# Create your views here.
class Authors(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        authors = Author.objects.all()[:10]
        data = AuthorSerializer(authors, many=True).data
        return Response(data)

    serializer_class = AuthorSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        author = AuthorSerializer(data=request.data['author'])
        if author.is_valid():
            b = author.save()
            return Response(author.data, status=status.HTTP_201_CREATED)
        else:
            return Response(author.errors, status=status.HTTP_400_BAD_REQUEST)

class AuthorDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        author = get_object_or_404(Author, pk=pk)
        data = AuthorSerializer(author).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        author = get_object_or_404(Author, pk=pk)
        ms = AuthorSerializer(author, data=request.data['author'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        author = get_object_or_404(Author, pk=pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
