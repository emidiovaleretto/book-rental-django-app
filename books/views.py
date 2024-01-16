from django.shortcuts import render
from django.views.generic import ListView
from .models import BookTitle, Book


class BookTitleListView(ListView):
    model = BookTitle
    context_object_name = "books"
    

def book_title_detail_view(request, pk):
    obj = BookTitle.objects.get(pk=pk)
    books = obj.books
    context = {
        'obj': obj,
        'books': books
    }
    return render(request, 'books/detail.html', context=context)
