from django.urls import path
from .views import HomePageView, AboutPageView, BooksDetails, BookIndiviView, BookCreateView, BookUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('booklist/', BooksDetails.as_view(), name='booklist'),
    path('booknew/', BookCreateView.as_view(), name='bookcreate'),
    path('booklist/<int:pk>/', BookIndiviView.as_view(), name='bookdetails'),
    # path('booklist/<int:pk>/edit', BookUpdateView, name='book_edit'),
    path('booklist/<int:pk>/edit', BookUpdateView.as_view(), name='book_edit'),
    # path('booklist/', BooksDetails, name='booklist'),
]
