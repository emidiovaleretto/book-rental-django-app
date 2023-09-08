from django.db import models
from books.models import Book
from django.utils.text import slugify


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, unique=True)
    additional_info = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(default=50)
    books = models.ManyToManyField(
        Book, 
        blank=True, 
        help_text="Books that are currently rented by this customer"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username or f"{self.first_name} {self.last_name}"
    
    def save(self, *args, **kwargs):
        if not self.username:
            self.username = slugify(self.__str__())
            username_exists = Customer.objects.filter(username=self.username).exists()

            while username_exists:
                self.username += f"-{Customer.objects.count() + 1}"
                username_exists = Customer.objects.filter(username=self.username).exists()

        super().save(*args, **kwargs)
