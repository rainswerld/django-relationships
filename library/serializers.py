from rest_framework import serializers

from .models.book import Book
from .models.author import Author
from .models.borrower import Borrower
from .models.loan import Loan

class BookSerializer(serializers.ModelSerializer):
  class Meta:
    model = Book
    fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'

class BorrowerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Borrower
    fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
  class Meta:
      model = Loan
      fields = '__all__'
