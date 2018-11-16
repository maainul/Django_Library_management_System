from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length=30)
    address=models.TextField(max_length=100)
    phone=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=50,unique=True)
    pub_date=models.DateField()
    number_copies=models.IntegerField()
    code_number=models.CharField(max_length=30,unique=True)
    price = models.IntegerField()
    add_date=models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    publication=models.ForeignKey(Publication,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Borrower(models.Model):
    name= models.CharField(max_length=20)
    gender    = models.CharField(max_length=10)
    address   = models.TextField(max_length=200)
    phone     = models.IntegerField()
    email     = models.EmailField()
    
    def __str__(self):
        return self.name

class Issu(models.Model):
    book_name    = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrower     = models.ForeignKey(Borrower,on_delete=models.CASCADE)
    created_date = models.DateField()
    expired_date = models.DateField()
    return_date  = models.DateField(null=True,blank=True)
    fine         = models.IntegerField(null=True,blank=True)

    def __str(self):
        return self.book_name
