from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post, PostReview
from django.utils.text import slugify
from django.shortcuts import get_object_or_404


class TestWorkappViewsAndModels(TestCase):
    """
    Test cases for workapp app as logged in user
    """
    def setUp(self):
        """ Setup test """
        username = 'adammmmadaaAA'
        password = '*456MoleManeeer'
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )
        logged_in = self.client.login(username=username, password=password)
        self.assertTrue(logged_in)

        # Create Post
        post = Post.objects.create(
            title='Test title',
            slug=slugify(f'{"Test title"}-{self.user}'),
            username=self.user,
            description='test description',
            contact_info='test@contact.com',
            rate=0,
            post_type=0,
            featured_image='placeholder'
            )

        # Create Reviews for Post
        review1 = PostReview.objects.create(
            title='Test review 1',
            post=get_object_or_404(Post.objects, title='Test title'),
            username=self.user,
            rating=2.5
            )

        review2 = PostReview.objects.create(
            title='Test review 2',
            post=get_object_or_404(Post.objects, title='Test title'),
            username=self.user,
            rating=5
            )

        review3 = PostReview.objects.create(
            title='Test review 3',
            post=get_object_or_404(Post.objects, title='Test title'),
            username=self.user,
            rating=4
            )

    def test_post_string_method_returns_name(self):
        """ Test Post Model string method """
        post = get_object_or_404(Post.objects, title='Test title')
        self.assertEqual(str(post), 'Test title')

    def test_post_avg_rating_method(self):
        """ Test Post Model avg_rating method """
        post = get_object_or_404(Post.objects, title='Test title')
        self.assertEqual(str(post.avg_rating()), '3.8')

    def test_post_reviews_total_method(self):
        """ Test Post Model reviews_total method """
        post = get_object_or_404(Post.objects, title='Test title')
        self.assertEqual(post.reviews_total(), 3)

    def test_post_review_string_method_returns_name(self):
        """ Test PostReview Model string method """
        review = get_object_or_404(PostReview.objects, title='Test review 1')
        self.assertEqual(str(review), 'Test review 1')

    def test_bulletin_board_home(self):
        """ Test Bulletin Board Home """
        response = self.client.get('/bulletin/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/bulletin_home.html')

    def test_bulletin_board_services(self):
        """ Test Bulletin Board Services """
        response = self.client.get('/bulletin/services/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/bulletin.html')

    def test_bulletin_board_requests(self):
        """ Test Bulletin Board Requests """
        response = self.client.get('/bulletin/requests/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/bulletin.html')

    def test_post_detail(self):
        """ Test Post Detail """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/bulletin/{post.slug}/{post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/post_detail.html')

    def test_post_create(self):
        """ Test Post Create """
        response = self.client.get('/post_create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/post_create.html')

    def test_post_edit(self):
        """ Test Post Edit """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/post_edit/{post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/post_edit.html')

    def test_post_delete(self):
        """ Test Post Delete """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/post_delete/{post.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/post_delete_success.html')

    def test_profile_page(self):
        """ Test Profile Page """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/profile/{post.username.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/profile.html')

    def test_review_create(self):
        """ Test Review Create """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/post_review_create/{post.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workapp/post_review_create.html')


class TestWorkappViewsLoggedOut(TestCase):
    """
    Test cases for workapp app as logged out user
    """
    def setUp(self):
        """ Setup test """
        username = 'adammmmadaaAA'
        password = '*456MoleManeeer'
        user_model = get_user_model()
        # Create user
        self.user = user_model.objects.create_user(
            username=username,
            password=password,
            is_superuser=True
        )

        # Create Post
        post = Post.objects.create(
            title='Test title',
            slug=slugify(f'{"Test title"}-{self.user}'),
            username=self.user,
            description='test description',
            contact_info='test@contact.com',
            rate=0,
            post_type=0,
            featured_image='placeholder'
            )

    def test_post_create(self):
        """ Test Post Create """
        response = self.client.get('/post_create/')
        self.assertEqual(response.status_code, 302)

    def test_post_edit(self):
        """ Test Post Edit """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/post_edit/{post.id}/')
        self.assertEqual(response.status_code, 302)

    def test_post_delete(self):
        """ Test Post Delete """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/post_delete/{post.id}/')
        self.assertEqual(response.status_code, 302)

    def test_review_create(self):
        """ Test Review Create """
        post = get_object_or_404(Post.objects, title='Test title')
        response = self.client.get(f'/post_review_create/{post.pk}/')
        self.assertEqual(response.status_code, 302)
