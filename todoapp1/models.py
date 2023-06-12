from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Categorie(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.title}'

class Todo(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.fields.TextField()
    category = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.title}'


