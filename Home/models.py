from django.db import models

# Create your models here.

class contact_me(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
    message = models.TextField()        

    def __str__(self):
        return self.name