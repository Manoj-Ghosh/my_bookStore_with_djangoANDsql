from django.shortcuts import render

# Create your views here.

from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "book_outlet/index.html", { "books" : books})

def book_detail(request, id):
    book = Book.objects.get(pk = id)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })

