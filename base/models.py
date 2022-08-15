from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    thumbnail = models.ImageField(null=True, blank=None, upload_to="images", default="placeholder.png")
    tags = models.ManyToManyField(Tag, null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if self.slug == None:
            slug = slugify(self.title)

            has_slug = Post.objects.filter(slug=slug).exists()

            count = 1

            while has_slug:
                count += 1
                slug = slugify(self.title) + '-' + str(count)

                has_slug = Post.objects.filter(slug=slug).exists()
            
            self.slug = slug
        super().save(*args, **kwargs)
    

