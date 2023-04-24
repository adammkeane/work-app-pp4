from django.test import TestCase


class TestHomeViews(TestCase):
    """
    Test cases for home app
    """
    def test_home_page(self):
        """ Test Home Page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
