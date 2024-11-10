from django.urls import path
from .views import list_books , LibraryDetailView
urlpatterns = [
    path('', view.list_book, name = "list"),
    path("library/", LibraryDetailView.as_view(), name = "library")

]