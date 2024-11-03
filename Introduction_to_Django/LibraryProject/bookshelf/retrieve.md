# Assuming you have a Book model defined in Django

# Command to retrieve and display all attributes of the book
from bookshelf.models import Book
book = Book.objects.get(title= '1984')

# Expected Output:
# {
#     'id': 1,
#     'title': '1984',
#     'author': 'George Orwell',
#     'year': 1949,
#     'genre': 'Dystopian',
#     'created_at': datetime.datetime(...),
#     'updated_at': datetime.datetime(...)
# }