from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Post, PostReview
from .forms import PostForm, PostReviewForm


class BulletinHome(generic.TemplateView):
    """View to show the bulletin home page"""
    template_name = 'workapp/bulletin_home.html'


class PostListService(generic.ListView):
    """View to show only service posts"""
    model = Post
    queryset = Post.objects.filter(post_type=0).order_by('-created_on')
    template_name = 'workapp/bulletin.html'
    paginate_by = 5


class PostListRequest(generic.ListView):
    """View to show only request posts"""
    model = Post
    queryset = Post.objects.filter(post_type=1).order_by('-created_on')
    template_name = 'workapp/bulletin.html'
    paginate_by = 5


class PostDetail(View):
    """View to show the details of a post"""
    def get(self, request, slug, id, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug, id=id)
        reviews = post.post_review.order_by('-created_on')
        if len(reviews) > 0:
            no_reviews = False
        else:
            no_reviews = True

        return render(
            request,
            'workapp/post_detail.html',
            {
                'post': post,
                'reviews': reviews,
                'no_reviews': no_reviews,
            },
        )


class PostCreate(UserPassesTestMixin, View):
    """View to handle post creation"""
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'workapp/post_create.html',
            {
                'post_form': PostForm(),
            },
        )

    def post(self, request, *args, **kwargs):
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            entry = post_form.save(commit=False)
            entry.username = request.user
            entry.slug = slugify(f'{entry.title}-{entry.username}')
            entry.save()
            post = get_object_or_404(Post.objects, id=entry.pk)

            return render(
                request,
                'workapp/post_create_success.html',
                {
                    'post': post,
                },
            )
        else:
            return render(
                request,
                'workapp/post_create.html',
                {
                    'post_form': PostForm(data=request.POST),
                },
            )

    def test_func(self):
        """Mixin Test"""
        return self.request.user.is_authenticated


class PostEdit(UserPassesTestMixin, View):
    """View to handle post editing"""
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=post_id)
        if post.username == self.request.user:
            return render(
                request,
                'workapp/post_edit.html',
                {
                    'post_form': PostForm(instance=post),
                    'post': post,
                },
            )
        else:
            return render(
                request,
                '403.html',
            )

    def post(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=post_id)
        post_form = PostForm(request.POST, request.FILES, instance=post)

        if post_form.is_valid():
            entry = post_form.save(commit=False)
            entry.username = request.user
            entry.slug = slugify(f'{entry.title}-{entry.username}')
            entry.save()

            return render(
                request,
                'workapp/post_edit_success.html',
                {
                    'post': post,
                },
            )

        else:
            return render(
                request,
                'workapp/post_edit.html',
                {
                    'post_form': PostForm(instance=post),
                    'post': post,
                },
            )

    def test_func(self):
        """Mixin Test"""
        return self.request.user.is_authenticated


class PostDelete(UserPassesTestMixin, View):
    """View to handle post deletion"""
    def get(self, request, post_id, *args, **kwargs):
        post = get_object_or_404(Post.objects, id=post_id)
        if post.username == self.request.user:
            user = post.username.pk
            post.delete()
            return render(
                        request,
                        'workapp/post_delete_success.html',
                        {
                            'user': user,
                        },
                    )
        else:
            return render(
                request,
                '403.html',
            )

    def test_func(self):
        """Mixin Test"""
        return self.request.user.is_authenticated


class ProfilePage(generic.ListView):
    """View to handle profile page display"""
    model = Post
    template_name = 'workapp/profile.html'
    pagenate_by = 10

    def get_queryset(self):
        """Gets only the posts the user in question has created"""
        return Post.objects.filter(username=self.kwargs.get('user'))


class PostReviewCreate(UserPassesTestMixin, View):
    """View to handle post review creation"""
    def get(self, request, post_id, *args, **kwargs):
        return render(
            request,
            'workapp/post_review_create.html',
            {
                'post_form': PostReviewForm(),
                'post_id': post_id
            },
        )

    def post(self, request, post_id, *args, **kwargs):
        post_form = PostReviewForm(request.POST)

        if post_form.is_valid():
            """If review form is valid, add review to database"""
            entry = post_form.save(commit=False)
            entry.username = request.user
            entry.slug = slugify(f'{entry.title}-{entry.username}')
            post = get_object_or_404(Post.objects, id=post_id)
            entry.post = post
            entry.save()

            return render(
                request,
                'workapp/post_review_create_success.html',
                {
                    'post': post,
                },
            )
        else:
            """If review form is not valid, return to form page"""
            return render(
                request,
                'workapp/post__review_create.html',
                {
                    'post_form': PostReviewForm(data=request.POST),
                },
            )

    def test_func(self):
        """Mixin Test"""
        return self.request.user.is_authenticated
