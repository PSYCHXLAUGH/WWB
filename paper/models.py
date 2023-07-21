from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse



class Paper(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Статьи на сайте'
        verbose_name_plural = 'Статьи на сайте'
        ordering = ['-time_create', 'title']


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # db_index - поле будет индексировано
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории на сайте'
        verbose_name_plural = 'Категории на сайте'
        ordering = ['-id', 'name']