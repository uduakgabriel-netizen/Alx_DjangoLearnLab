# Query all books by a specific author.
# List all books in a library.
# Retrieve the librarian for a library.


from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
def books_by_author(author):
    try:
        # author = Author.objects.get(name=author_name)
        author = Author.objects.filter(author=author)
        return author.books.all()
    except Author.DoesNotExist:
        return []

# Query 2: List all books in a library
def books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Query 3: Retrieve the librarian for a library
def librarian_of_library(library):
    try:
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None