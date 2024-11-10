from django.shortcuts import render

from .models import  Author, Book, Library, Librarian

from django.views.generic import ListView , DetailView

def list_book(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html", {"books": books})


class details_library(ListView):

    model = Library 

# Create your views here.
