from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products, category_list

"""
@skip("demonstrating skipping")
class TestSkip(TestCase):
    def test_skip_example(self):
        pass
"""

# simulate a user accessing the view
# so we need to tool to do that there two option here
# first option --> from django test we have a clinet


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, created_by_id=1, title='Django Book',
                               slug='django-book', price='30.00', image='djangobook')

    # Test Home Page url
    def test_url_allowed_hosts(self):
        """
        Test Allowed Hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """
        Test category list Response Status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_store_url(self):
        """
        Test Store url
        """
        request = HttpRequest()
        response = category_list(request)
        self.assertEqual(response.status_code, 200)

    def test_product_details_url(self):
        """
        Test Product details Response Status
        """
        response = self.c.get(reverse('store:product_details', args=['django-book']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Test Homepage Html Code
        """
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # option two --> using request factory
    # in this we are test function as function
    # And this actually best than to kind of go through the approach of browser with Clinet

    def test_view_function(self):
        """
        Test View Function using Factory
        """
        request = self.factory.get('/item/django-book/')
        response = all_products(request)
        html = response.content.decode('utf8')
        # print(html)
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
