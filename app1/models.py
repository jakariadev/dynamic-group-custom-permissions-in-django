from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse
class Books(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    pageno = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('canedittitle',
             'can edit title on books'),
            ('canaddpageno',
             'can add pageno on books')
        )


    def get_absolute_url(self):  # new
        return reverse('booklist')

    def __str__(self):
        return self.title


class BooksPopularity(models.Model):
    title = models.ForeignKey(Books, on_delete=models.CASCADE)
    popularity = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
