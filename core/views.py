from django.shortcuts import render, get_object_or_404
from customers.models import Customer
from books.models import Book, BookTitle

def home_view(request):
    customers = Customer.objects.all()
    obj = get_object_or_404(BookTitle, id=2)
    books = obj.books
    title = obj.title
    publisher = obj.publisher
    context = {
        'books': books,
        'customers': customers,
        'title': title,
        'publisher': publisher,
    }
    return render(request, 'main.html', context=context)