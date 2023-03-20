from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm


class BulletinHome(generic.TemplateView):
    template_name = 'bulletin_home.html'


class PostListService(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, post_type=0).order_by('-created_on')
    template_name = 'bulletin.html'
    paginate_by = 5


class PostListRequest(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1, post_type=1).order_by('-created_on')
    template_name = 'bulletin.html'
    paginate_by = 5


class PostDetail(View):

    def get(self, request, slug, id, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug, id=id)

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
            {
                'post_form': PostForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        # post_type = request.POST["post_type"]
        # title = request.POST["title"]
        # slug = request.POST["slug"]
        # username = request.POST["username"]
        # description = request.POST["description"]
        # featured_image = request.POST["featured_image"]
        # blurb = request.POST["blurb"]
        # payment_type = request.POST["payment_type"]
        # rate = request.POST["rate"]
        # status = request.POST["status"]

        # post = Post(
        #     post_type=post_type,
        #     title=title,
        #     slug=slug,
        #     username=username,
        #     description=description,
        #     featured_image=featured_image,
        #     blurb=blurb,
        #     payment_type=payment_type,
        #     rate=rate,
        #     status=status,
        #     )

        post_form = PostForm(data=request.POST)
        # post = get_object_or_404(Post.objects, slug=request.POST["slug"])

        if post_form.is_valid():
            entry = post_form.save()
            entry.slug = slugify(f'{entry.title}-{entry.username}')
            entry.save()
        else:
            post_form = PostForm()

        post = get_object_or_404(Post.objects, id=entry.pk)

        return render(
            request,
            'post_create_success.html',
            {
                'post': post,
            },
        )


class ProfilePage(generic.ListView):
    model = Post
    template_name = 'profile.html'
    pagenate_by = 10

    def get_queryset(self):
        return Post.objects.filter(username=self.kwargs.get('user'))
