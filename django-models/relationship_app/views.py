from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm



def list_book(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):

    model = Library 
    template_name = "relationship_app/library_detail.html"

# Create your views here.
