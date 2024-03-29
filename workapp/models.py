from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

POST_TYPE = ((0, "Service"), (1, "Request"))
PAYMENT_TYPE = ((0, "Per Hour"), (1, "Total Payment"))


class Post(models.Model):
    post_type = models.IntegerField(choices=POST_TYPE, default=0)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_posts"
        )
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=4000)
    featured_image = CloudinaryField('image', default='placeholder')
    blurb = models.TextField(blank=True, max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    payment_type = models.IntegerField(choices=PAYMENT_TYPE, default=0)
    rate = models.PositiveIntegerField(default=0)
    contact_info = models.TextField(max_length=400)

    class Meta:
        # ordered in descending order, based on created_on value,
        # so that newest posts are first.
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def just_date_created_on(self):
        """Simplfies date"""
        return self.created_on.date()

    def just_date_updated_on(self):
        """Simplfies date"""
        return self.updated_on.date()

    def avg_rating(self):
        """Calculates the mean average rating of a post"""
        reviews = self.post_review.all()
        if len(reviews) > 0:
            review_total = 0
            for review in reviews:
                review_total += review.rating
            avg_rating_raw = (review_total)/(len(reviews))
            avg_rating = round(avg_rating_raw, 1)
            return avg_rating
        else:
            return 'N/A'

    def reviews_total(self):
        """Counts number of reviews a post has"""
        reviews = self.post_review.all()
        return len(reviews)


RATING = (
    (0, "0"),
    (0.5, "0.5"),
    (1, "1"),
    (1.5, "1.5"),
    (2, "2"),
    (2.5, "2.5"),
    (3, "3"),
    (3.5, "3.5"),
    (4, "4"),
    (4.5, "4.5"),
    (5, "5")
    )


class PostReview(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_review"
        )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_review"
        )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=55)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=10000)
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        choices=RATING, max_digits=2, decimal_places=1
        )

    class Meta:
        # ordered in descending order, based on created_on value,
        # so that newest posts are first.
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def just_date_created_on(self):
        """Simplfies date"""
        return self.created_on.date()

    def just_date_updated_on(self):
        """Simplfies date"""
        return self.updated_on.date()
