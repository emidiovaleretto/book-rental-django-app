from django.db import models


class Author(models.Model):
    """
    Book author model
    Managed only in django admin
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name