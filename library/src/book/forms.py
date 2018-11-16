from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from book.models import Author,Publication,Borrower,Category
from book.models import Book,Issu


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('name', 'email', 'phone')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save author'))


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = ('name', 'address', 'phone','email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save publication'))


class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = ('name', 'gender', 'phone','email','address')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save borrower'))


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save category'))


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'pub_date', 'number_copies','code_number','price','add_date','author','category','publication')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save book'))


class IssuForm(forms.ModelForm):
    class Meta:
        model = Issu
        fields = ('book_name', 'borrower', 'created_date','expired_date','return_date','fine')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save issu'))