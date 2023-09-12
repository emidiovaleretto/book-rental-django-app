from django.urls import path
from .views import book_title_list_view

urlpatterns = [
    path("", book_title_list_view, name="book_title_list_view"),
]