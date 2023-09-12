from django.urls import path
from .views import book_title_list_view, book_title_detail_view

urlpatterns = [
    path("", book_title_list_view, name="book_title_list_view"),
    path("<int:pk>/", book_title_detail_view, name="book_title_detail_view"),
]