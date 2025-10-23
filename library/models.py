from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to="items/", blank=True, null=True)
    categories = models.ManyToManyField(Category, related_name="items", blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    library_name = models.CharField(max_length=150)
    url = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="posts", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.library_name