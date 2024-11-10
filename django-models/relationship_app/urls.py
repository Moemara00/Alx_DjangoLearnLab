from django.urls import path
from . import views
from .views import list_books , LibraryDetailView
urlpatterns = [
    path('',views.list_book, name = "list"),
    path("library/", LibraryDetailView.as_view(), name = "library")

]