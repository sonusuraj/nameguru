from django.db import models

# Create your models here.
class Name(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=25)
    gender = models.CharField(max_length=2,default='m')
    meaning = models.CharField(max_length=191, default=None)
    religion = models.CharField(max_length=2,default='h')
