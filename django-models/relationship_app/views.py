from django.shortcuts import render
from .models import Library, Book
from django.views.generic.detail import DetailView 
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


def list_book(request):
    books = Book.objects.all()

    return render(request,"relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):

    model = Library 
    template_name = "relationship_app/library_detail.html"


class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'





# Create your views here.
