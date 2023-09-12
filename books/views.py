from django.shortcuts import render
from .models import BookTitle, Book


def book_title_list_view(request):
    queryset = BookTitle.objects.all()
    print(queryset)
    context = {
        'object_list': queryset
    }
    print(context['object_list'])
    return render(request, 'books/main.html', context=context)

def book_title_detail_view(request, pk):
    obj = BookTitle.objects.get(pk=pk)
    books = obj.books
    context = {
        'obj': obj,
        'books': books
    }
    return render(request, 'books/detail.html', context=context)
