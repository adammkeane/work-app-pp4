from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
POST_TYPE = ((0, "Service"), (1, "Request"))
PAYMENT_TYPE = ((0, "Per Hour"), (1, "Total Payment"), (2, "Job Dependant"))


class Post(models.Model):

    post_type = models.IntegerField(choices=POST_TYPE, default=0)
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=55, unique=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts")
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    blurb = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE, default=0)
    rate = models.PositiveIntegerField(default=0)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        # ordered in descending order, based on created_on value, so that newest posts are first.
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def just_date(self):
        return self.created_on.date()