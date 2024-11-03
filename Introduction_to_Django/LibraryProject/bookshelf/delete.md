# Command to delete the book with the title "Nineteen Eighty-Four"
from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="Nineteen Eighty-Four")  # Assuming this title exists
book.delete()  # Delete the book

# Confirm the deletion by trying to retrieve all books
books = Book.objects.all()

# Expected Output:
# If the deletion was successful, the list of books will not include "Nineteen Eighty-Four"
# print(books)  # This should return a QuerySet with all other books except "Nineteen Eighty-Four"
