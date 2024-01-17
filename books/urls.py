from django.urls import path
from .views import BookTitleListView, BookTitleDetailView

urlpatterns = [
    path("", BookTitleListView.as_view(), name="book_title_list_view"),
    path("<int:pk>/", BookTitleDetailView.as_view(), name="book_title_detail_view"),
]