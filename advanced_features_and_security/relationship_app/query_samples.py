#Query all books by a specific author

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:
        # Use filter to get all books by the author
        author = Author.objects.get(name=author_name)
        return Book.objects.filter(author=author)
    except Author.DoesNotExist:
        return None


# List all books in a library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None


# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        # Correct query: get the librarian associated with the library
        return Librarian.objects.get(library=library)
    except Library.DoesNotExist:
        return None
    except Librarian.DoesNotExist:
        return None