from django.test import TestCase
from django.db.models import DecimalField, CharField, ImageField, BooleanField, DateTimeField

from shop.models import Product


class TestProductFieldType(TestCase):
    def test_name_field_type(self):
        assert_same_type(self, "name", CharField)

    def test_price_field_type(self):
        assert_same_type(self, "price", DecimalField)

    def test_img_field_type(self):
        assert_same_type(self, "img", ImageField)

    def test_onsale_field_type(self):
        assert_same_type(self, "on_sale", BooleanField)


def assert_same_type(self, field_name, field_type):
    self.assertTrue(
        isinstance(
            get_product_field(field_name),
            field_type
        )
    )


def get_product_field(field_name):
    return Product._meta.get_field(field_name)