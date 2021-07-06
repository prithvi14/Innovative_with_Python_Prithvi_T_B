from django.db import models

# Create your models here.

class Person(models.Model):
    Name = models.CharField(max_length=20)
    Contact = models.IntegerField()
    Address = models.TextField(blank=True)

    def __str__(self):
        return self.Name
