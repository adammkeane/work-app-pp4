from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'bulletin.html'
    pagenate_by = 10


class PostDetail(View):

    def get(self, request, slug, id, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug, id=id)

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
            },
        )