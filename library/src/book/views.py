from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from book.models import Author,Publication,Borrower,Category,Book,Issu
from book.forms import AuthorForm,PublicationForm,BorrowerForm,CategoryForm
from book.forms import BookForm,IssuForm


class AuthorListView(ListView):
    model = Author
    context_object_name = 'book'


class AuthorCreateView(CreateView):
    model = Author
    fields = ('name', 'email', 'phone')
    success_url = reverse_lazy('author_list')


class AuthorUpdateView(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author_update_form.html'
    success_url = reverse_lazy('author_list')


class PublicationListView(ListView):
	model = Publication
	context_object_name = 'book'


class PublicationCreateView(CreateView):
	model = Publication
	fields = ('name', 'address', 'phone','email')
	success_url = reverse_lazy('publication_list')


class PublicationUpdateView(UpdateView):
    model = Publication
    form_class = PublicationForm
    template_name = 'book/publication_update_form.html'
    success_url = reverse_lazy('publication_list')


class BorrowerListView(ListView):
    model = Borrower
    context_object_name = 'book'


class BorrowerCreateView(CreateView):
    model = Borrower
    fields = ('name','gender','phone', 'email','address')
    success_url = reverse_lazy('borrower_list')


class BorrowerUpdateView(UpdateView):
    model = Borrower
    form_class = BorrowerForm
    template_name = 'book/borrower_update_form.html'
    success_url = reverse_lazy('borrower_list')


class CategoryListView(ListView):
    model = Category
    context_object_name = 'book'


class CategoryCreateView(CreateView):
    model = Category
    fields = ('name','description')
    success_url = reverse_lazy('category_list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'book/category_update_form.html'
    success_url = reverse_lazy('category_list')

class BookListView(ListView):
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    fields = ('name', 'pub_date', 'number_copies','code_number','price','add_date','author','category','publication')
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book_update_form.html'
    success_url = reverse_lazy('book_list')


class IssuListView(ListView):
    model = Issu
    context_object_name = 'book'


class IssuCreateView(CreateView):
    model = Issu
    fields = ('book_name', 'borrower', 'created_date','expired_date','return_date','fine')
    success_url = reverse_lazy('issu_list')


class IssuUpdateView(UpdateView):
    model = Issu
    form_class = IssuForm
    template_name = 'book/issu_update_form.html'
    success_url = reverse_lazy('issu_list')
