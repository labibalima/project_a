from django.db import models

# Create your models here.

class retust(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    class_of_student = models.IntegerField()
    def __str__(self):
        return f"My name is {self.name} My age is {self.age} and I am read in class {self.class_of_student}"