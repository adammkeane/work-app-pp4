from .models import Post
from django import forms
from django.utils.translation import gettext_lazy as _


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'post_type',
            'title',
            'username',
            'description',
            'featured_image',
            'blurb',
            'payment_type',
            'rate',
            'status',
            )
        labels = {
            'rate': _('Rate (€)'),
        }