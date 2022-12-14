from django.db import models

# Create your models here.
class Post(models.Model):
    image1 = models.ImageField(upload_to='post/images')
    image2 = models.ImageField(upload_to='post/images')
    image3 = models.ImageField(upload_to='post/images')
    image4 = models.ImageField(upload_to='post/images', null=True)
    image5 = models.ImageField(upload_to='post/images', null=True)
    
    proj_title = models.TextField()
    proj_start = models.DateField(null=True)
    proj_end = models.DateField(null=True)
    proj_exp = models.TextField()
    proj_url = models.URLField()
    proj_team = models.TextField()
    proj_stack = models.TextField(null=True)
    
    
    def get_absolute_url(self):
        return f'/{self.pk}/'
    
    
    def __str__(self):
        return self.proj_title