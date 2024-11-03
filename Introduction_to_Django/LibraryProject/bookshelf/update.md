from bookshelf.models import Book

# Retrieve the book instance
book = Book.objects.get(title="1984")  # Assuming this title exists
book.title = "Nineteen Eighty-Four"  # Update the title
book.save()  # Save the changes

# Expected Output:
# The title of the book is now: Nineteen Eighty-Four