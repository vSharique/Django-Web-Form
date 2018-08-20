from django.db import models

# Create your models here.


class UserData (models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(max_length=50)
    ph = models.CharField(max_length=10)

    def __str__(self):
        return self.name

