from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    admin_category = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    is_published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}. {self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
