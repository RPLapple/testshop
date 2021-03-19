from django.test import TestCase
from django.urls import resolve

from shop.views import shop_view


class TestShopPageView(TestCase):
    # 期望found.func.__name__ == shop_view.__name__
    def test_resolve_shop(self):
        found = resolve('/shop/')
        self.assertEqual(found.func.__name__, shop_view.__name__)

    # 期望 status_code 會等於 200 (也就是正常)
    def test_reachable_shop(self):
        response = self.client.get('/shop/')
        self.assertEqual(response.status_code, 200)

    # 期望這頁面的 template 是 shop/shop.html 這個檔案
    def test_template_shop(self):
        response = self.client.get('/shop/')
        self.assertTemplateUsed(response, 'shop/shop.html')

    # 期望這頁面的標題是 RS Django Sho
    def test_title_shop(self):
        response = self.client.get('/shop/')
        self.assertContains(response, 'RS Django Shop')