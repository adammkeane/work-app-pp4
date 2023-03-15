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

    def post(self, request, *args, **kwargs):
        post_type = request.POST["post_type"]
        title = request.POST["title"]
        slug = request.POST["slug"]
        username = request.POST["username"]
        description = request.POST["description"]
        featured_image = request.POST["featured_image"]
        blurb = request.POST["blurb"]
        payment_type = request.POST["payment_type"]
        rate = request.POST["rate"]
        status = request.POST["status"]

        post = Post(
            post_type=post_type,
            title=title,
            slug=slug,
            username=username,
            description=description,
            featured_image=featured_image,
            blurb=blurb,
            payment_type=payment_type,
            rate=rate,
            status=status,
            )

        post.save()

        return render(
            request,
            'post_detail.html',
            {
                'post': post,
            },
        )


class PostCreate(View):
    def get(self, request, *args, **kwargs):

        return render(
            request,
            'post_create.html',
        )