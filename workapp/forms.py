from .models import Post, PostReview
from django import forms
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from cloudinary.forms import CloudinaryFileField


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'post_type',
            'title',
            'description',
            'featured_image',
            'blurb',
            'payment_type',
            'rate',
            'contact_info',
        )
        labels = {
            'rate': _('Rate (€)'),
            'featured_image': _(
                'Featured Image (shown on the Bulletin Board. '
                'If no file uploaded, the default SideHustle '
                'image will be used)'
                ),
            'blurb': _('Blurb (max 200 characters)'),
            'contact_info': _(
                'Contact Info (how other users will contact '
                'you about your post)'
                )
        }
        widgets = {
            'description': SummernoteWidget(),
        }


class PostReviewForm(forms.ModelForm):
    class Meta:
        model = PostReview
        fields = (
                'title',
                'description',
                'rating',
            )
