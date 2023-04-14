from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from shop_app.models import Offer, Stocks, Product, Order, UserProfile
from shop_app.views import UserCreate
from shop_app.forms import MyUserCreateForm


class PersonalAccountViewTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test_user', password='123456789')
        self.stocks = Stocks.objects.create(name='test_stock', discount=99)
        self.product = Product.objects.create(name='test_product', price=999)
        self.offers = Offer.objects.create(product=self.product, discount=99)
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.order = Order.objects.create(user_profile=self.user_profile)
        self.product.order_set.add(self.order)
        self.client.force_login(self.user)

    def tearDown(self):
        self.user.delete()
        self.product.delete()
        self.user_profile.delete()

    def test_personal_account_view(self):
        response = self.client.get(reverse('shop:account'))
        self.assertTemplateUsed(response, 'shop_app/account.html')
        self.assertContains(response, 'test_stock')
        self.assertContains(response, 'test_product')
        self.stocks.delete()
        self.offers.delete()
        self.order.delete()

        response = self.client.get(reverse('shop:account'))
        self.assertNotContains(response, 'test_stock')
        self.assertNotContains(response, 'test_product')
        self.assertContains(response, _('Скидок нет'))
        self.assertContains(response, _('Предложений нет'))
        self.assertContains(response, _('Список заказов пуст'))

        self.client.logout()
        response = self.client.get(reverse('shop:account'))
        self.assertRedirects(response, '{}?next=/account/'.format(reverse('shop:login')))


class UserLoginViewTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test_user', password='123456789')

    def tearDown(self):
        self.user.delete()

    def test_user_login_view(self):
        response = self.client.get(reverse('shop:login'))
        self.assertTemplateUsed(response, 'shop_app/login.html')

        response = self.client.post(reverse('shop:login'), {'username': 'test_user',
                                                            'password': '123456789'})
        self.assertRedirects(response, reverse('shop:main'))


class UserLogoutViewTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test_user', password='123456789')
        self.client.force_login(self.user)

    def tearDown(self):
        self.user.delete()

    def test_user_logout_view(self):
        response = self.client.get(reverse('shop:logout'))
        self.assertRedirects(response, reverse('shop:main'))


class UserCreateTestCase(TestCase):
    def test_user_create(self):
        self.assertEqual(UserCreate().get_form_class(), MyUserCreateForm)
        response = self.client.post(reverse('shop:user_create'), {'username': 'test_user',
                                                                  'password1': '123456789',
                                                                  'password2': '123456789'})
        self.assertTemplateUsed(response, 'shop_app/user_create.html')
        self.assertRedirects(response, reverse('shop:main'))
