from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Picture(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    images = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.title