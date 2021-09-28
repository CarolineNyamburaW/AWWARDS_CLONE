from django.db import models
import datetime as dt
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100, null=False, blank=False)

  def __str__(self):
      return self.name

class Photo(models.Model):
  category = models.ForeignKey( Category, on_delete=models.SET_NULL, null=True, blank=True )
  image = CloudinaryField('image', default = '')
  description= models.TextField()

  def __str__(self):
      return self.description

class Site(models.Model):
    image = CloudinaryField('image')
    title = models.CharField( max_length=70)
    description = models.CharField( max_length=200)
    link = models.URLField( )
    created_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def save_image(self):
        self.save()