from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
    ordering = ('created_at',)

admin.site.register(Customer, CustomerAdmin)
