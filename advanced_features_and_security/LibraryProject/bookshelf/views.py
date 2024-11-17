from django.shortcuts import render
from .forms import ExampleForm
# Create your views here.
from django.contrib.auth.decorators import  permission_required


from django.http import HttpResponse

@permission_required('bookshelf.CustomUser', raise_exception = True)
def say_message(request):

    book_list = ['']
    HttpResponse("Hello")