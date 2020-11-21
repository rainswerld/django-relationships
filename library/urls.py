from django.urls import path

from .views.book_views import Books, BookDetail
from .views.author_views import Authors, AuthorDetail

urlpatterns = [
    path('authors', Authors.as_view(), name='authors'),
    path('authors/<int:pk>', AuthorDetail.as_view(), name='author_detail'),
    path('books', Books.as_view(), name='books'),
    path('books/<int:pk>', BookDetail.as_view(), name='book_detail'),
]
