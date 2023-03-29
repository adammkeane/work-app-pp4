from .models import Post
from django import forms
from django.utils.translation import gettext_lazy as _
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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
            'status',
            )
        labels = {
            'rate': _('Rate (€)'),
            'featured_image': _('Featured Image (shown on the Bulletin Board)'),
        }
        widgets = {
            'description': SummernoteWidget(),
        }