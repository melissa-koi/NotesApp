from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)

class Notes(models.Model):
    heading = models.CharField(max_length=200)
    text = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.heading