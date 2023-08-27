from django.db import models
from django.db.models import CharField

from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False)

    def get_absolute_url(self) -> str:
        return reverse(viewname='book:authors-detail', kwargs={'pk': self.pk})

    def __str__(self) -> CharField:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE,
                               null=False, blank=False, related_name='books')

    def __str__(self) -> CharField:
        return self.title
