# from django.test import TestCase
# from rest_framework.test import APITestCase
# from django.urls import reverse
# from api.models import Book
# from django.contrib.auth import get_user_model
# # from rest_framework.test import APITestCase
# from rest_framework import status
# # from django.urls import reverse
# from django.contrib.auth import get_user_model
# from api.models import Book
# import datetime

# # class BookAPITest(APITestCase):
# class BookAPITest(APITestCase):
#     """
#     Test suite for the Book API endpoints covering CRUD, filtering, searching,
#     ordering, and authentication/permissions.
#     """

#     def setUp(self):
#         """
#         Set up common data for all tests in this class.
#         This runs before each test method.
#         """
#         self.list_url = reverse('book-list')  # URL for listing and creating books
        
#         # Create a non-admin user for authenticated tests
#         self.user = User.objects.create_user(
#             username='testuser', 
#             password='testpassword'
#         )
#         # Create an admin user for permission tests
#         self.admin_user = User.objects.create_superuser(
#             username='adminuser',
#             email='admin@example.com',
#             password='adminpassword'
#         )

#         # Create initial books for testing
#         self.book1 = Book.objects.create(
#             title="The Lord of the Rings", 
#             author="J.R.R. Tolkien",
#             publication_date=datetime.date(1954, 7, 29)
#         )
#         self.book2 = Book.objects.create(
#             title="The Hobbit", 
#             author="J.R.R. Tolkien",
#             publication_date=datetime.date(1937, 9, 21)
#         )
#         self.book3 = Book.objects.create(
#             title="Dune", 
#             author="Frank Herbert",
#             publication_date=datetime.date(1965, 8, 1)
#         )
        
#         # URL for a specific book detail
#         self.book1_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})


#     # --- CRUD Operation Tests ---

#     def test_create_book_authenticated(self):
#         """
#         Ensure we can create a new book with valid data when authenticated.
#         """
#         self.client.force_authenticate(user=self.user) # Authenticate the client
#         data = {
#             'title': 'Foundation',
#             'author': 'Isaac Asimov',
#             'publication_date': '1951-06-01'
#         }
#         response = self.client.post(self.list_url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Book.objects.count(), 4) # Check if book count increased
#         self.assertEqual(response.data['title'], 'Foundation')
#         self.assertEqual(response.data['author'], 'Isaac Asimov')
#         self.assertEqual(response.data['publication_date'], '1951-06-01')

#     def test_create_book_unauthenticated(self):
#         """
#         Ensure unauthenticated users cannot create a book.
#         """
#         data = {
#             'title': 'Unauth Book',
#             'author': 'No One',
#             'publication_date': '2000-01-01'
#         }
#         response = self.client.post(self.list_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.assertEqual(Book.objects.count(), 3) # Book count should remain unchanged

#     def test_create_book_invalid_data(self):
#         """
#         Ensure creating a book with invalid data returns a 400 Bad Request.
#         """
#         self.client.force_authenticate(user=self.user)
#         data = {
#             'title': '',  # Invalid: title is required
#             'author': 'Test Author',
#             'publication_date': '2023-01-01'
#         }
#         response = self.client.post(self.list_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn('title', response.data) # Check for error on 'title' field
#         self.assertEqual(Book.objects.count(), 3)

#     def test_list_books_succeeds(self):
#         """
#         Ensure retrieving the list of books works correctly.
#         """
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 3) # Check initial book count

#     def test_retrieve_single_book_succeeds(self):
#         """
#         Ensure retrieving a single book by ID works.
#         """
#         response = self.client.get(self.book1_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], self.book1.title)
#         self.assertEqual(response.data['author'], self.book1.author)

#     def test_retrieve_non_existent_book_fails(self):
#         """
#         Ensure requesting a non-existent book returns 404 Not Found.
#         """
#         non_existent_url = reverse('book-detail', kwargs={'pk': 999})
#         response = self.client.get(non_existent_url)
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

#     def test_update_book_patch_authenticated(self):
#         """
#         Ensure a book can be partially updated when authenticated.
#         """
#         self.client.force_authenticate(user=self.user)
#         data = {'author': 'Updated Author'}
#         response = self.client.patch(self.book1_detail_url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.book1.refresh_from_db() # Reload book data from the database
#         self.assertEqual(self.book1.author, 'Updated Author')
#         self.assertEqual(response.data['author'], 'Updated Author')
#         # Ensure other fields remain unchanged
#         self.assertEqual(self.book1.title, "The Lord of the Rings")

#     def test_update_book_put_authenticated(self):
#         """
#         Ensure a book can be fully updated when authenticated.
#         """
#         self.client.force_authenticate(user=self.user)
#         data = {
#             'title': 'New Title for Book 1',
#             'author': 'New Author for Book 1',
#             'publication_date': '2020-01-01'
#         }
#         response = self.client.put(self.book1_detail_url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.book1.refresh_from_db()
#         self.assertEqual(self.book1.title, 'New Title for Book 1')
#         self.assertEqual(self.book1.author, 'New Author for Book 1')
#         self.assertEqual(self.book1.publication_date, datetime.date(2020, 1, 1))

#     def test_update_book_unauthenticated(self):
#         """
#         Ensure unauthenticated users cannot update a book.
#         """
#         data = {'title': 'Should Not Update'}
#         response = self.client.patch(self.book1_detail_url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.book1.refresh_from_db()
#         self.assertNotEqual(self.book1.title, 'Should Not Update') # Ensure no change

#     def test_delete_book_authenticated(self):
#         """
#         Ensure a book can be deleted when authenticated.
#         """
#         self.client.force_authenticate(user=self.user)
#         response = self.client.delete(self.book1_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Book.objects.count(), 2) # Verify book is deleted
#         self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

#     def test_delete_book_unauthenticated(self):
#         """
#         Ensure unauthenticated users cannot delete a book.
#         """
#         response = self.client.delete(self.book1_detail_url)
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.assertEqual(Book.objects.count(), 3) # Book count should remain unchanged

#     # --- Filtering Tests ---

#     def test_filter_by_publication_year(self):
#         """
#         Ensure filtering by publication_year works.
#         """
#         response = self.client.get(self.list_url, {'publication_year': 1954})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['title'], "The Lord of the Rings")

#     def test_filter_by_author_icontains(self):
#         """
#         Ensure filtering by author (case-insensitive contains) works.
#         """
#         response = self.client.get(self.list_url, {'author': 'tolkien'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)
#         # Ensure both Tolkien books are present (order might vary, so check titles)
#         titles = {book['title'] for book in response.data}
#         self.assertIn("The Lord of the Rings", titles)
#         self.assertIn("The Hobbit", titles)

#     # --- Search Tests ---

#     def test_search_by_title_or_author(self):
#         """
#         Ensure searching across title and author fields works.
#         """
#         response = self.client.get(self.list_url, {'search': 'hobbit'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['title'], "The Hobbit")

#         response = self.client.get(self.list_url, {'search': 'frank'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['author'], "Frank Herbert")

#     def test_search_no_match(self):
#         """
#         Ensure search with no matching results returns an empty list.
#         """
#         response = self.client.get(self.list_url, {'search': 'nonexistent'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 0)

#     # --- Ordering Tests ---

#     def test_order_by_title_ascending(self):
#         """
#         Ensure ordering by title in ascending order works.
#         """
#         response = self.client.get(self.list_url, {'ordering': 'title'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # Assuming alphabetical order: Dune, Hobbit, Lord of the Rings
#         self.assertEqual(response.data[0]['title'], "Dune")
#         self.assertEqual(response.data[1]['title'], "The Hobbit")
#         self.assertEqual(response.data[2]['title'], "The Lord of the Rings")

#     def test_order_by_publication_date_descending(self):
#         """
#         Ensure ordering by publication_date in descending order works.
#         """
#         response = self.client.get(self.list_url, {'ordering': '-publication_date'})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         # Correct order by publication_date descending: Dune (1965), Lord of the Rings (1954), The Hobbit (1937)
#         self.assertEqual(response.data[0]['title'], "Dune")
#         self.assertEqual(response.data[1]['title'], "The Lord of the Rings")
#         self.assertEqual(response.data[2]['title'], "The Hobbit")

#     # --- Combined Functionality Tests ---

#     def test_combined_filter_search_order(self):
#         """
#         Ensure all functionalities work together.
#         Example: Find Tolkien books, search for 'Lord', order by title descending.
#         """
#         # Create another Tolkien book to ensure search and filter work well
#         Book.objects.create(
#             title="Children of Húrin", 
#             author="J.R.R. Tolkien",
#             publication_date=datetime.date(2007, 4, 17) # A much newer book
#         )
        
#         response = self.client.get(self.list_url, {
#             'publication_year': 1954, # Filter: specific year
#             'search': 'Rings',        # Search: part of title
#             'ordering': 'title'       # Order: by title
#         })
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['title'], "The Lord of the Rings")


#     # --- Permission Tests (if applicable, assuming Book creation/update requires authentication) ---

#     def test_list_books_unauthenticated_access(self):
#         """
#         Ensure unauthenticated users can view the list of books (read-only access).
#         """
#         self.client.force_authenticate(user=None) # Ensure no user is authenticated
#         response = self.client.get(self.list_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertGreater(len(response.data), 0) # Should return books

#     def test_update_book_unauthorized_permission(self):
#         """
#         If update requires specific permissions (e.g., admin), test a non-admin user.
#         (This test assumes a permission class like IsAdminUser on the detail view)
#         """
#         # If you had a custom permission like 'IsAdminUser' on BookDetail:
#         # self.client.force_authenticate(user=self.user) # Non-admin user
#         # data = {'title': 'Forbidden Update'}
#         # response = self.client.patch(self.book1_detail_url, data, format='json')
#         # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) # Expected if IsAdminUser
#         pass # Placeholder if no specific forbidden test is needed for non-admin users.

#     def test_delete_book_unauthorized_permission(self):
#         """
#         If delete requires specific permissions (e.g., admin), test a non-admin user.
#         """
#         # Similar to update, if a custom permission is applied.
#         # self.client.force_authenticate(user=self.user) # Non-admin user
#         # response = self.client.delete(self.book1_detail_url)
#         # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#         pass # Placeholder if no specific forbidden test is needed for non-admin users.


# myapp/tests.py

from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book, Author
# from ..models import Book # Assuming Book model is in a parent directory
import datetime

User = get_user_model() 

class BookAPITest(APITestCase):
    """
    Test suite for the Book API endpoints covering CRUD, filtering, searching,
    ordering, and authentication/permissions.
    """

    def setUp(self):
        """
        Set up common data for all tests in this class.
        This runs before each test method.
        """
        self.list_url = reverse('book-list')  # URL for listing and creating books
        
        # Create a non-admin user for authenticated tests
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword'
        )
        # Create an admin user for permission tests
        self.admin_user = User.objects.create_superuser(
            username='adminuser',
            email='admin@example.com',
            password='adminpassword'
        )
        
        # First, create the Author instances
        self.tolkien = Author.objects.create(name="J.R.R. Tolkien")
        self.herbert = Author.objects.create(name="Frank Herbert")
        self.asimov = Author.objects.create(name="Isaac Asimov")

        # Create initial books for testing
        self.book1 = Book.objects.create(
            title="The Lord of the Rings", 
            author=self.tolkien, # Pass the Author object
            publication_date=datetime.date(1954, 7, 29)
        )
        self.book2 = Book.objects.create(
            title="The Hobbit", 
            author=self.tolkien, # Pass the Author object
            publication_date=datetime.date(1937, 9, 21)
        )
        self.book3 = Book.objects.create(
            title="Dune", 
            author=self.herbert, # Pass the Author object
            publication_date=datetime.date(1965, 8, 1)
        )
        
        # URL for a specific book detail
        self.book1_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})


    # --- CRUD Operation Tests ---

    def test_create_book_authenticated(self):
        """
        Ensure we can create a new book with valid data when authenticated.
        """
        self.client.force_authenticate(user=self.user) # Authenticate the client
        data = {
            'title': 'Foundation',
            'author': self.asimov.id, # Pass the Author object's ID
            'publication_date': '1951-06-01'
        }
        response = self.client.post(self.list_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4) # Check if book count increased
        self.assertEqual(response.data['title'], 'Foundation')
        self.assertEqual(response.data['author'], self.asimov.id) # Check for the author's ID
        self.assertEqual(response.data['publication_date'], '1951-06-01')

    def test_create_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot create a book.
        """
        data = {
            'title': 'Unauth Book',
            'author': self.asimov.id, # Pass the Author object's ID
            'publication_date': '2000-01-01'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3) # Book count should remain unchanged

    def test_create_book_invalid_data(self):
        """
        Ensure creating a book with invalid data returns a 400 Bad Request.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': '',  # Invalid: title is required
            'author': self.asimov.id, # Pass the Author object's ID
            'publication_date': '2023-01-01'
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data) # Check for error on 'title' field
        self.assertEqual(Book.objects.count(), 3)

    def test_list_books_succeeds(self):
        """
        Ensure retrieving the list of books works correctly.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) # Check initial book count
        # Check that the author field is the ID
        self.assertEqual(response.data[0]['author'], self.book1.author.id)

    def test_retrieve_single_book_succeeds(self):
        """
        Ensure retrieving a single book by ID works.
        """
        response = self.client.get(self.book1_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['author'], self.book1.author.id)

    def test_retrieve_non_existent_book_fails(self):
        """
        Ensure requesting a non-existent book returns 404 Not Found.
        """
        non_existent_url = reverse('book-detail', kwargs={'pk': 999})
        response = self.client.get(non_existent_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_book_patch_authenticated(self):
        """
        Ensure a book can be partially updated when authenticated.
        """
        self.client.force_authenticate(user=self.user)
        data = {'author': self.herbert.id} # Pass the Author object's ID
        response = self.client.patch(self.book1_detail_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db() # Reload book data from the database
        self.assertEqual(self.book1.author.name, 'Frank Herbert')
        self.assertEqual(response.data['author'], self.herbert.id)
        # Ensure other fields remain unchanged
        self.assertEqual(self.book1.title, "The Lord of the Rings")

    def test_update_book_put_authenticated(self):
        """
        Ensure a book can be fully updated when authenticated.
        """
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'New Title for Book 1',
            'author': self.herbert.id, # Pass the Author object's ID
            'publication_date': '2020-01-01'
        }
        response = self.client.put(self.book1_detail_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'New Title for Book 1')
        self.assertEqual(self.book1.author.name, 'Frank Herbert')
        self.assertEqual(self.book1.publication_date, datetime.date(2020, 1, 1))

    def test_update_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot update a book.
        """
        data = {'title': 'Should Not Update'}
        response = self.client.patch(self.book1_detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.book1.refresh_from_db()
        self.assertNotEqual(self.book1.title, 'Should Not Update') # Ensure no change

    def test_delete_book_authenticated(self):
        """
        Ensure a book can be deleted when authenticated.
        """
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.book1_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2) # Verify book is deleted
        self.assertFalse(Book.objects.filter(pk=self.book1.pk).exists())

    def test_delete_book_unauthenticated(self):
        """
        Ensure unauthenticated users cannot delete a book.
        """
        response = self.client.delete(self.book1_detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 3) # Book count should remain unchanged

    # --- Filtering Tests ---

    def test_filter_by_publication_year(self):
        """
        Ensure filtering by publication_year works.
        """
        response = self.client.get(self.list_url, {'publication_year': 1954})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Lord of the Rings")

    def test_filter_by_author_icontains(self):
        """
        Ensure filtering by author (case-insensitive contains) works.
        """
        response = self.client.get(self.list_url, {'author': 'tolkien'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        # Ensure both Tolkien books are present (order might vary, so check titles)
        titles = {book['title'] for book in response.data}
        self.assertIn("The Lord of the Rings", titles)
        self.assertIn("The Hobbit", titles)

    # --- Search Tests ---

    def test_search_by_title_or_author(self):
        """
        Ensure searching across title and author fields works.
        """
        response = self.client.get(self.list_url, {'search': 'hobbit'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

        response = self.client.get(self.list_url, {'search': 'frank'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.herbert.id) # Check for ID

    def test_search_no_match(self):
        """
        Ensure search with no matching results returns an empty list.
        """
        response = self.client.get(self.list_url, {'search': 'nonexistent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    # --- Ordering Tests ---

    def test_order_by_title_ascending(self):
        """
        Ensure ordering by title in ascending order works.
        """
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming alphabetical order: Dune, Hobbit, Lord of the Rings
        self.assertEqual(response.data[0]['title'], "Dune")
        self.assertEqual(response.data[1]['title'], "The Hobbit")
        self.assertEqual(response.data[2]['title'], "The Lord of the Rings")

    def test_order_by_publication_date_descending(self):
        """
        Ensure ordering by publication_date in descending order works.
        """
        response = self.client.get(self.list_url, {'ordering': '-publication_date'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Correct order by publication_date descending: Dune (1965), Lord of the Rings (1954), The Hobbit (1937)
        self.assertEqual(response.data[0]['title'], "Dune")
        self.assertEqual(response.data[1]['title'], "The Lord of the Rings")
        self.assertEqual(response.data[2]['title'], "The Hobbit")

    # --- Combined Functionality Tests ---

    def test_combined_filter_search_order(self):
        """
        Ensure all functionalities work together.
        """
        # Create another Tolkien book to ensure search and filter work well
        Book.objects.create(
            title="Children of Húrin", 
            author=self.tolkien,
            publication_date=datetime.date(2007, 4, 17) # A much newer book
        )
        
        response = self.client.get(self.list_url, {
            'publication_year': 1954, # Filter: specific year
            'search': 'Rings',        # Search: part of title
            'ordering': 'title'       # Order: by title
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Lord of the Rings")


    # --- Permission Tests ---

    def test_list_books_unauthenticated_access(self):
        """
        Ensure unauthenticated users can view the list of books (read-only access).
        """
        self.client.force_authenticate(user=None) # Ensure no user is authenticated
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0) # Should return books

    def test_update_book_unauthorized_permission(self):
        """
        Test a non-admin user cannot update if permissions are restricted.
        """
        pass # This test is a placeholder

    def test_delete_book_unauthorized_permission(self):
        """
        Test a non-admin user cannot delete if permissions are restricted.
        """
        pass # This test is a placeholder