from django.shortcuts import render
from .models import BookTitle


def book_title_list_view(request):
    queryset = BookTitle.objects.all()
    print(queryset)
    context = {
        'object_list': queryset
    }
    print(context['object_list'])
    return render(request, 'books/main.html', context=context)
