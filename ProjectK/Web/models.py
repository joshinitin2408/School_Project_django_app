from django.db import models

# Create your models here.
class Admission(models.Model):
     Father = models.CharField(max_length=200)
     FatherOccupation = models.CharField(max_length=200)
     Mother = models.CharField(max_length=200)
     MotherOccupation = models.CharField(max_length=200)
     Child = models.CharField(max_length=200)
     Age = models.CharField(max_length=200)
     Address = models.CharField(max_length=200)
     Mobile = models.CharField(max_length=200)
     Division = models.CharField(max_length=200)
     Description = models.TextField()
     Date=models.DateField()

     def __str__(self):
          return self.Child +' '+ 'S/O' + ' ' + self.Father

class Contact(models.Model):
     Name = models.CharField(max_length=100)
     Mobile = models.CharField(max_length=100)
     Message = models.TextField()
     def __str__(self):
          return self.Name
