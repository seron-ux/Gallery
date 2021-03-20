from django.db import models

# Create your models here.
class Image(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    location = models.TextField(max_length=30,null=False,blank=False, default='')
    image=models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now = True)