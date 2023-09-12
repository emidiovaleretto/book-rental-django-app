import uuid

from django.db import models
from django.utils.text import slugify
from django.core.files import File

from publishers.models import Publishers
from authors.models import Author

import qrcode
from io import BytesIO
from PIL import Image



class BookTitle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(blank=True)
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def books(self):
        return self.get_books()

    def get_books(self):
        return self.my_books.all()

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Book(models.Model):
    isbn = models.CharField(max_length=24, blank=True)
    title = models.ForeignKey(BookTitle, on_delete=models.CASCADE, related_name='my_books')
    publisher = models.ForeignKey(Publishers, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_isbn(self):
        """
        Generate a unique book ID
        """
        self.isbn = str(uuid.uuid4()).replace('-', '')[:24].lower()
        return self.isbn

    def generate_qrcode(self):
        """
        Generate a QR Code for the isbn
        """
        qrcode_img = qrcode.make(self.isbn)
        canvas = Image.new('RGB', (qrcode_img.pixel_size, qrcode_img.pixel_size), 'white')
        canvas.paste(qrcode_img)

        fname = f'qr_code-{str(self.isbn).lower()}.png'
        buffer = BytesIO()

        canvas.save(buffer, 'PNG')

        self.qr_code.save(fname, File(buffer), save=False)

        canvas.close()


    def save(self, *args, **kwargs):
        if not self.isbn:
            self.generate_isbn()

        if not self.qr_code:
            self.generate_qrcode()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title.title
    