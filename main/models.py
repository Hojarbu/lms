from django.core.validators import RegexValidator
from django.db import models

# Create your models here.


class LibUser(models.Model):
    full_name = models.CharField(max_length=128, verbose_name='Full name')
    phone_regex = RegexValidator(regex=r'^\d{9}$',
                                 message="Up to 13 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=13)
    email = models.EmailField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.full_name}'

    class Meta:
        verbose_name = 'Library user'
        verbose_name_plural = 'Library users'


class Book(models.Model):
    title = models.CharField(max_length=260)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='books')
    published_year = models.IntegerField(null=True, blank=True)
    author = models.CharField(max_length=260)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class PurchasedBook(models.Model):
    lib_user = models.ForeignKey(LibUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True)
    duration = models.PositiveSmallIntegerField(verbose_name='Days count')
    return_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.date}' or f'{self.pk}'

    class Meta:
        verbose_name = 'Purchased Book'
        verbose_name_plural = 'Purchased Books'