from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='python', slug='python')

    def test_category_models_entry(self):
        """
        Test category model data insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_models_entry_1(self):
        """
        Test Category Return name
        """

        data = self.data1
        self.assertEqual(str(data), 'python')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='python', slug='python')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, created_by_id=1, title='Python Book',
                                            slug='python-book', price='20.00', image='pythonbook')

    def test_product_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """

        data = self.data1
        self.assertTrue(isinstance(data, Product))  # Just Test the name of attributes
        self.assertEqual(str(data), 'Python Book')  # You must write Capital
