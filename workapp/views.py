from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Post, PostReview
from .forms import PostForm, PostReviewForm


class BulletinHome(generic.TemplateView):
    template_name = 'workapp/bulletin_home.html'


class PostListService(generic.ListView):
    model = Post
    queryset = Post.objects.filter(post_type=0).order_by('-created_on')
    template_name = 'workapp/bulletin.html'
    paginate_by = 5


class PostListRequest(generic.ListView):
    model = Post
    queryset = Post.objects.filter(post_type=1).order_by('-created_on')
    template_name = 'workapp/bulletin.html'
    paginate_by = 5


class PostDetail(View):
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
        return self.request.user.is_authenticated


class PostEdit(UserPassesTestMixin, View):
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
        return self.request.user.is_authenticated


class PostDelete(UserPassesTestMixin, View):
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
        return self.request.user.is_authenticated


class ProfilePage(generic.ListView):
    model = Post
    template_name = 'workapp/profile.html'
    pagenate_by = 10

    def get_queryset(self):
        return Post.objects.filter(username=self.kwargs.get('user'))


class PostReviewCreate(UserPassesTestMixin, View):
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
            return render(
                request,
                'workapp/post__review_create.html',
                {
                    'post_form': PostReviewForm(data=request.POST),
                },
            )

    def test_func(self):
        return self.request.user.is_authenticated
