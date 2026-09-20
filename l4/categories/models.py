from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField("Category", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
