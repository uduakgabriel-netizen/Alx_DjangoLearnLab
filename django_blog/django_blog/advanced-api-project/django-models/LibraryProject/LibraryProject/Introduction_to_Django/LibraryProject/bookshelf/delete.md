from bookshelf.models import Book

new_book = Book.objects.get(title="Nineteen Eighty-Four") new_book.delete()

(1, {'bookshelf.Book': 1})
Confirm deletion