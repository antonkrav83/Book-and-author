from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    cat = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True) 

    def __str__(self):
        return self.name   