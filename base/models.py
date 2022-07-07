from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    #thumbnail
    tags = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return self.title
    

