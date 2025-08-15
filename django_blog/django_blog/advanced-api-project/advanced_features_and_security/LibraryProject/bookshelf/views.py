from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm


# Create your views here.

@permission_required('bookshelf.can_delete', raise_exception=True)
@permission_required('bookshelf.can_create', raise_exception=True)
@permission_required('bookshelf.can_edit', raise_exception=True)
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list_view(request):
    book_list = Book.objects.all()
    context = {'book_list': book_list}
    return render(request, 'bookshelf/book_list.html', context)
