from django.contrib import admin

# Register your models here.
from main.models import LibUser, Book, PurchasedBook

admin.site.register(LibUser)
admin.site.register(Book)
admin.site.register(PurchasedBook)