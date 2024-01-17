from django import forms
from .models import BookTitle


class BookTitleForm(forms.ModelForm):
    
    class Meta:
        model = BookTitle
        fields = ('title', 'publisher', 'authors',)

    def clean(self):
        title = self.cleaned_data.get('title')

        if len(title) <= 5:
            error_msg = 'The title must have at least 6 characters.'
            self.add_error('title', error_msg)

        book_title_exists = BookTitle.objects.filter(
            title__iexact=title
        ).exists()

        if book_title_exists:
            error_msg = 'This book title already exists in our database.'
            self.add_error('title', error_msg)

        return self.cleaned_data