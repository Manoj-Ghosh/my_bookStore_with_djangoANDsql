from django.shortcuts import render

from django.http import Http404
from django.db.models import Avg, Max, Min

from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Book

def index(request):
    books = Book.objects.all().order_by("title") # by assending order of title
    #books = Book.objects.all().order_by("-title") --> by assending order of title
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating")) # rating__avg


    return render(request, "book_outlet/index.html", { 
        "books" : books,
        "total_number_of_books": num_books,
        "average_rating" : avg_rating
        
    })

def book_detail(request, slug):

    # try:

    #     book = Book.objects.get(pk = id)

    # except:
    #     raise Http404()
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", {
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_bestseller": book.is_bestselling
    })

