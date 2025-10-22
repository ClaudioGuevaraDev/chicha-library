from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to="items/")
    categories = models.ManyToManyField(Category, related_name="items", blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name