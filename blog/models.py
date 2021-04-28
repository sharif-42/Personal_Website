from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField()
    image = models.ImageField()
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
