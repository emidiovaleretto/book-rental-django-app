from django.db import models
from books.models import Book
from customers.models import Customer

from datetime import timedelta

from . import STATUS_CHOICES


class Rental(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='#0')
    
    rented_at = models.DateTimeField(
        help_text="Date and time when the book was rented"
    )
    due_at = models.DateTimeField(
        blank=True,
        help_text="Date and time when the book is due"
    )
    returned_at = models.DateTimeField(
        null=True,
        blank=True, 
        help_text="Date and time when the book was returned"
    )
    is_closed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} rented by {self.customer.username}"
    
    def save(self, *args, **kwargs):
        if not self.due_at:
            self.due_at = self.rented_at + timedelta(days=14)
        super().save(*args, **kwargs)

