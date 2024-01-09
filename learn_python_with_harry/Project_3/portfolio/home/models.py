from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(default="", max_length=200)
    phone = models.CharField(default="", max_length=200)
    email = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.name} - {self.email}"