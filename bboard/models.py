from tabnanny import verbose

from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 20, db_index = True, verbose_name = 'category')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        ordering = ['name']

class BBoard(models.Model):

    title = models.CharField(max_length = 20, verbose_name = 'title')
    price = models.FloatField(verbose_name = 'price')
    content = models.TextField(verbose_name = 'content')
    user = models.CharField(max_length = 20, verbose_name = 'user')
    date = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name = 'date')

    category = models.ForeignKey('Category', null = True, on_delete = models.PROTECT, verbose_name = 'category')

    class Meta:
        verbose_name_plural = 'announcements'
        verbose_name = 'announcement'
        ordering = ['date']