from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'post_type',
            'title',
            'slug',
            'username',
            'description',
            'featured_image',
            'blurb',
            'payment_type',
            'rate',
            'status',
            )