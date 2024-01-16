from django.urls import path
from .views import BookTitleListView, book_title_detail_view

urlpatterns = [
    path("", BookTitleListView.as_view(), name="book_title_list_view"),
    path("<int:pk>/", book_title_detail_view, name="book_title_detail_view"),
]