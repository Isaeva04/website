
from django.db import models
class services(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.FileField(upload_to='img/')