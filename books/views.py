from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BookTitle, Book


class BookTitleListView(ListView):
    model = BookTitle
    context_object_name = "books"
    template_name = "books/main.html"
    ordering = ('-created_at',)


class BookTitleDetailView(DetailView):
    model = BookTitle
    context_object_name = "book"
    template_name = "books/detail.html"
        
    

# def book_title_detail_view(request, pk):
#     obj = BookTitle.objects.get(pk=pk)
#     books = obj.books
#     context = {
#         'obj': obj,
#         'books': books
#     }
#     return render(request, 'books/detail.html', context=context)
