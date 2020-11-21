from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.borrower import Borrower
from ..serializers import BorrowerSerializer

# Create your views here.
class Borrowers(APIView):
    def get(self, request):
        """Index Request"""
        borrowers = Borrower.objects.all()[:10]
        data = BorrowerSerializer(borrowers, many=True).data
        return Response(data)

    serializer_class = BorrowerSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        borrower = BorrowerSerializer(data=request.data['borrower'])
        if borrower.is_valid():
            b = borrower.save()
            return Response(borrower.data, status=status.HTTP_201_CREATED)
        else:
            return Response(borrower.errors, status=status.HTTP_400_BAD_REQUEST)

class BorrowerDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        borrower = get_object_or_404(Borrower, pk=pk)
        print(borrower.loans.all())
        data = BorrowerSerializer(borrower).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        borrower = get_object_or_404(Borrower, pk=pk)
        ms = BorrowerSerializer(borrower, data=request.data['borrower'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        borrower = get_object_or_404(Borrower, pk=pk)
        borrower.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
