from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    Author = models.ForeignKey(get_user_model(),on_delete = models.CASCADE)

    Created_date = models.DateTimeField
    Published_date = models.DateTimeField