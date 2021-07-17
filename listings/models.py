from django.db import models
from realtors.models import University

class Member (models.Model):
    university=models.ForeignKey(University,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    address=models.TextField(blank=True)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)

    def __str__(self):
        return self.name





