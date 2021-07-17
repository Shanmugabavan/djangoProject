from django.db import models

# Create your models here.

class University(models.Model):
    uni_name=models.CharField(max_length=255)
    uni_address=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    phone_number=models.IntegerField()

    def __str__(self):
        return self.uni_name


