from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=100)
    description=models.TextField()
    image=models.FileField(upload_to='img/')

class services(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.FileField(upload_to='img/')