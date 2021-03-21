from django.db import models

# Create your models here.
class Image(models.Model):
    caption = models.CharField(max_length=100)
    title = models.CharField(max_length=200, default='')
    location = models.TextField(max_length=30,null=False,blank=False, default='')
    image=models.ImageField(upload_to='images/',default='image.jpg')
    category=models.CharField(max_length=200, default='')
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
    @classmethod
    def search_by_category(cls,search_term):
        pictures = cls.objects.filter(category__icontains=search_term)
        return pictures

   