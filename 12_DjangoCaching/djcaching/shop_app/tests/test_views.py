from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from shop_app.models import Offer, Stocks, Product, Order, UserProfile, Shop
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

        response = self.client.get(reverse('shop:user_create'))
        self.assertTemplateUsed(response, 'shop_app/user_create.html')

        response = self.client.post(reverse('shop:user_create'), {'username': 'test_user',
                                                                  'password1': 'test_123456789',
                                                                  'password2': 'test_123456789'})
        self.assertRedirects(response, reverse('shop:main'))


class ShopCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='test_user', password='user_12345678')
        cls.user_staff = User.objects.create_user(username='test_user_staff',
                                                  password='user_staff_12345678',
                                                  is_staff=True)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.user_staff.delete()

    def test_shop_create_view_user_not_staff(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:shop_create'))
        self.assertEqual(response.status_code, 403)
        self.client.logout()

        response = self.client.get(reverse('shop:shop_create'))
        self.assertRedirects(response, '{}?next=/shops/shop-create/'.format(reverse('shop:login')))

    def test_shop_create_view_user_staff(self):
        self.client.force_login(self.user_staff)
        response = self.client.get(reverse('shop:shop_create'))
        self.assertTemplateUsed(response, 'shop_app/shop_create.html')
        self.assertContains(response, '<h1>Добавить магазин:</h1>')
        self.assertContains(response, '<input type="hidden" name="csrfmiddlewaretoken"')
        self.assertContains(response, '<label for="id_name">Название:</label>')
        self.assertContains(response, '<input type="text" name="name" maxlength="20" required id="id_name">')
        self.assertContains(response, '<label for="id_address">Адрес:</label>')
        self.assertContains(response, '<input type="text" name="address" maxlength="100" required id="id_address">')
        self.assertContains(response, '<button type="submit">Добавить</button>')

        response = self.client.post(reverse('shop:shop_create'), {'name': 'shop_test_name',
                                                                  'address': 'shop_test_address'})
        self.assertRedirects(response, reverse('shop:shops'))

        response = self.client.get(reverse('shop:shops'))
        self.assertContains(response, 'shop_test_name / shop_test_address')
        self.assertContains(response, 'Список магазинов:')
        self.assertContains(response, 'Добавить магазин')
        self.assertContains(response, 'href="{}"'.format(reverse('shop:shop_create')))

        self.client.logout()
        response = self.client.get(reverse('shop:shops'))
        self.assertContains(response, 'Список магазинов:')
        self.assertContains(response, 'shop_test_name / shop_test_address')
        self.assertNotContains(response, 'Добавить магазин')
        self.assertNotContains(response, 'href="{}"'.format(reverse('shop:shop_create')))

        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:shops'))
        self.assertContains(response, 'Список магазинов:')
        self.assertContains(response, 'shop_test_name / shop_test_address')
        self.assertNotContains(response, 'Добавить магазин')
        self.assertNotContains(response, 'href="{}"'.format(reverse('shop:shop_create')))


class ProductsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='test_user', password='123456789')
        cls.user_staff = User.objects.create_user(username='test_user_staff', password='staff_123456789', is_staff=True)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.user_staff.delete()

    def setUp(self) -> None:
        self.product = Product.objects.create(name='test_product', description='test_description', price=999)

    def tearDown(self) -> None:
        self.product.delete()

    def test_product_views(self):
        self.client.force_login(self.user_staff)
        response = self.client.get(reverse('shop:products'))
        self.assertContains(response, '<h1>Список продуктов:</h1>')
        self.assertContains(response, 'test_product / test_description / 999')
        self.assertContains(response, 'Добавить продукт')
        self.assertContains(response, 'href="{}"'.format(reverse('shop:product_create')))

        self.client.logout()
        response = self.client.get(reverse('shop:products'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '{}?next=/products/'.format(reverse('shop:login')))
        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:products'))
        self.assertEqual(response.status_code, 403)


class ProductCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='test_user', password='123456789')
        cls.user_staff = User.objects.create_user(username='test_user_staff', password='staff_123456789', is_staff=True)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()
        cls.user_staff.delete()

    def test_product_create_view(self):
        self.client.force_login(self.user_staff)
        response = self.client.get(reverse('shop:product_create'))
        self.assertTemplateUsed(response, 'shop_app/product_create.html')
        self.assertContains(response, '<h1>Добавить продукт:</h1>')
        self.assertContains(response, '<input type="hidden" name="csrfmiddlewaretoken"')
        self.assertContains(response, '<label for="id_name">Название товара:</label>')
        self.assertContains(response, '<input type="text" name="name"')
        self.assertContains(response, '<label for="id_description">Описание товара:</label>')
        self.assertContains(response, '<input type="text" name="description" maxlength="100" required id="id_description">')
        self.assertContains(response, '<label for="id_price">Стоимость:</label>')
        self.assertContains(response, '<input type="number" name="price" step="0.01" required id="id_price">')
        self.assertContains(response, '<button type="submit">Добавить</button>')

        response = self.client.post(reverse('shop:product_create'), {'name': 'test_product',
                                                                     'description': 'test_description',
                                                                     'price': 999})
        self.assertRedirects(response, reverse('shop:products'))

        response = self.client.get(reverse('shop:products'))
        self.assertContains(response, 'test_product / test_description / 999')

        self.client.logout()
        response = self.client.get(reverse('shop:product_create'))
        self.assertRedirects(response, '{}?next=/products/product-create/'.format(reverse('shop:login')))

        self.client.force_login(self.user)
        response = self.client.get(reverse('shop:product_create'))
        self.assertEqual(response.status_code, 403)
