from django.db import models


class Student(models.Model):
    Name = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    Course = models.CharField(max_length=10)
    Year = models.IntegerField()

    def __str__(self):
        return self.Name

