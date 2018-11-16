from django.contrib import admin
from django.urls import path
from book.views import AuthorListView, AuthorCreateView, AuthorUpdateView
from book.views import PublicationListView, PublicationCreateView, PublicationUpdateView
from book.views import BorrowerListView, BorrowerCreateView, BorrowerUpdateView
from book.views import CategoryListView, CategoryCreateView, CategoryUpdateView
from book.views import BookListView, BookCreateView, BookUpdateView
from book.views import IssuListView, IssuCreateView, IssuUpdateView


urlpatterns = [
	path('admin/', admin.site.urls),
    
## Author 
    path('author_list', AuthorListView.as_view(), name='author_list'),
    path('author/add/', AuthorCreateView.as_view(), name='author_add'),
    path('author/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_edit'),

## Publication 
    path('publication/', PublicationListView.as_view(), name='publication_list'),
    path('publication/add/', PublicationCreateView.as_view(), name='publication_add'),
    path('publication/<int:pk>/edit/', PublicationUpdateView.as_view(), name='publication_edit'),

## Borrower
	path('borrower/',BorrowerListView.as_view(), name='borrower_list'),
    path('borrower/add/',BorrowerCreateView.as_view(), name='borrower_add'),
    path('borrower/<int:pk>/edit/',BorrowerUpdateView.as_view(), name='borrower_edit'),

## Category
    path('category/',CategoryListView.as_view(), name='category_list'),
    path('category/add/',CategoryCreateView.as_view(), name='category_add'),
    path('category/<int:pk>/edit/',CategoryUpdateView.as_view(), name='category_edit'),

## Book
    path('',BookListView.as_view(), name='book_list'),
    path('book/add/',BookCreateView.as_view(), name='book_add'),
    path('book/<int:pk>/edit/',BookUpdateView.as_view(), name='book_edit'),

## Borrow_book_info
    path('issu/',IssuListView.as_view(), name='issu_list'),
    path('issu/add/',IssuCreateView.as_view(), name='issu_add'),
    path('issu/<int:pk>/edit/',IssuUpdateView.as_view(), name='issu_edit'),
]
