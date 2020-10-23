from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)
    image = models.ImageField(upload_to=, )
    description = models.TextChoices()

    class Meta:


    def __str__(self):
        return self.name