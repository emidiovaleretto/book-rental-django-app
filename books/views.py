from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from .models import BookTitle, Book
from .forms import BookTitleForm


class BookTitleListView(FormView, ListView):
    model = BookTitle
    context_object_name = "books"
    template_name = "books/main.html"
    ordering = ('-created_at',)
    form_class = BookTitleForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        return super().form_invalid(form)


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
