# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

library = Library.objects.get(name=library_name)
library_books = library.books.all()
    


def create_sample_data():
    print("--- Creating Sample Data ---")

    # Create Authors
    author1 = Author.objects.create(name="Jane Doe")
    author2 = Author.objects.create(name="John Smith")
    author3 = Author.objects.create(name="Emily White")
    print(f"Created authors: {author1.name}, {author2.name}, {author3.name}")

    # Create Books and link them to Authors (ForeignKey)
    book1 = Book.objects.create(title="The First Journey", author=author1)
    book2 = Book.objects.create(title="Mysteries of the Deep", author=author1)
    book3 = Book.objects.create(title="Code Complete Guide", author=author2)
    book4 = Book.objects.create(title="The Art of Storytelling", author=author3)
    book5 = Book.objects.create(title="Advanced Python", author=author2)
    print(f"Created books: {book1.title}, {book2.title}, {book3.title}, {book4.title}, {book5.title}")

    # Create Libraries
    library1 = Library.objects.create(name="Central City Library")
    library2 = Library.objects.create(name="University Archives")
    print(f"Created libraries: {library1.name}, {library2.name}")
    
    # getting data from the libraries
    
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    

    # Add Books to Libraries (ManyToManyField)
    library1.books.add(book1, book2, book3)
    library2.books.add(book3, book4, book5)
    print(f"Assigned books to libraries.")

    # Create Librarians and link them to Libraries (OneToOneField)
    librarian1 = Librarian.objects.create(name="Alice Green", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Brown", library=library2)
    print(f"Created librarians: {librarian1.name}, {librarian2.name}")

    print("--- Sample Data Creation Complete ---")
    return author1, library1

def run_queries(author_to_query=None, library_to_query=None):
    print("\n--- Running Sample Queries ---")

    # Query 1: Query all books by a specific author.
    if author_to_query is None:
        try:
            author_to_query = Author.objects.first()
            if not author_to_query:
                print("No authors found in the database. Please create some data first.")
                return
        except Exception as e:
            print(f"Error getting author: {e}")
            return

    print(f"\n--- Books by {author_to_query.name} ---")
    books_by_author = author_to_query.books.all()
    if books_by_author:
        for book in books_by_author:
            print(f"- {book.title}")
    else:
        print(f"No books found for {author_to_query.name}.")

    # Query 2: List all books in a library.
    if library_to_query is None:
        try:
            library_to_query = Library.objects.first()
            if not library_to_query:
                print("No libraries found in the database. Please create some data first.")
                return
        except Exception as e:
            print(f"Error getting library: {e}")
            return

    print(f"\n--- Books in {library_to_query.name} ---")
    books_in_library = library_to_query.books.all()
    if books_in_library:
        for book in books_in_library:
            print(f"- {book.title}")
    else:
        print(f"No books found in {library_to_query.name}.")

    # Query 3: Retrieve the librarian for a library.
    print(f"\n--- Librarian for {library_to_query.name} ---")
    try:
        librarian_for_library = library_to_query.librarian
        print(f"The librarian is: {librarian_for_library.name}")
    except Librarian.DoesNotExist:
        print(f"No librarian found for {library_to_query.name}.")
    except Exception as e:
        print(f"Error retrieving librarian: {e}")

    print("\n--- Sample Queries Complete ---")
