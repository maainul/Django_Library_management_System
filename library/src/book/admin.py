from django.contrib import admin
from .models import Author,Publication
from .models import Borrower,Category,Issu,Book


admin.site.register(Author)

admin.site.register(Publication)

admin.site.register(Borrower)

admin.site.register(Category)

admin.site.register(Book)

admin.site.register(Issu)