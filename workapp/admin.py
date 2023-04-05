from django.contrib import admin
from .models import Post, PostReview
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title', 'username')}
    summernote_fields = ('description')

@admin.register(PostReview)
class PostReviewAdmin(admin.ModelAdmin):
    search_fields: ('title', 'description')
