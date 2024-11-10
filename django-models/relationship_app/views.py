from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView 

def list_book(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):

    model = Library 
    template_name = "relationship_app/library_detail.html"

# Create your views here.