from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.utils.text import slugify
from django.contrib.auth.models import User
from .models import Post, PostReview
from .forms import PostForm


class HomePage(generic.TemplateView):
    template_name = 'index.html'


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
        reviews = post.post_review.order_by('created_on')
        if len(reviews) > 0:
            no_reviews = False
        else:
            no_reviews = True
        
        return render(
            request,
            'post_detail.html',
            {
                'post': post,
                'reviews': reviews,
                'no_reviews': no_reviews,
            },
        )


class PostCreate(View):
    def get(self, request, *args, **kwargs):
        username = request.user.username
        return render(
            request,
            'post_create.html',
            {
                'post_form': PostForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            entry = post_form.save(commit=False)
            entry.username = request.user
            entry.slug = slugify(f'{entry.title}-{entry.username}')
            entry.save()
            post = get_object_or_404(Post.objects, id=entry.pk)

            return render(
                request,
                'post_create_success.html',
                {
                    'post': post,
                },
            )
        else:
            return render(
                request,
                'post_create.html',
                {
                    'post_form': PostForm(data=request.POST),
                },
            )


class PostEdit(View):
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=post_id)
        return render(
            request,
            'post_edit.html',
            {
                'post_form': PostForm(instance=post),
                'post': post,
            },
        )

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=post_id)
        post_form = PostForm(data=request.POST, instance=post)

        if post_form.is_valid():
            entry = post_form.save(commit=False)
            entry.username = request.user
            entry.slug = slugify(f'{entry.title}-{entry.username}')
            entry.save()

            return render(
                request,
                'post_edit_success.html',
                {
                    'post': post,
                },
            )

        else:
            return render(
                request,
                'post_edit.html',
                {
                    'post_form': PostForm(instance=post),
                    'post': post,
                },
            )


class PostDelete(View):
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=post_id)
        user = post.username.pk
        post.delete()
        return render(
                    request,
                    'post_delete_success.html',
                    {
                        'user': user,
                    },
                )


class ProfilePage(generic.ListView):
    model = Post
    template_name = 'profile.html'
    pagenate_by = 10

    def get_queryset(self):
        return Post.objects.filter(username=self.kwargs.get('user'))
