from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from ..models.loan import Loan
from ..serializers import LoanSerializer

# Create your views here.
class Loans(APIView):
    def get(self, request):
        """Index Request"""
        loans = Loan.objects.all()[:10]
        data = LoanSerializer(loans, many=True).data
        return Response(data)

    serializer_class = LoanSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        loan = LoanSerializer(data=request.data['loan'])
        if loan.is_valid():
            b = loan.save()
            return Response(loan.data, status=status.HTTP_201_CREATED)
        else:
            return Response(loan.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        loan = get_object_or_404(Loan, pk=pk)
        data = LoanSerializer(loan).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        loan = get_object_or_404(Loan, pk=pk)
        ms = LoanSerializer(loan, data=request.data['loan'])
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        loan = get_object_or_404(Loan, pk=pk)
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
