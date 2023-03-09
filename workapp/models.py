from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):

    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=105, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    blurb = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        # ordered in descending order, based on created_on value, so that newest posts are first.
        ordering = ['-created_on']

    def __str__(self):
        return self.title
