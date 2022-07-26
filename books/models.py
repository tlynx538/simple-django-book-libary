from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=255)