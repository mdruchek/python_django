from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from app_blogs.models import Blog


class BlogDetailViewTestCase(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user: User = User.objects.create_user(username='user_test', password='u12345678')
        perm_view_blog = Permission.objects.get(
            codename='view_blog'
        )
        cls.user.user_permissions.add(perm_view_blog, )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.blog = Blog.objects.create(
            author=self.user,
            content='test content'
        )

    def tearDown(self) -> None:
        self.blog.delete()

    def test_blog_detail_view(self):
        response = self.client.get(reverse('app_blogs:detail',
                                           kwargs={'pk': self.blog.pk}))
        self.assertContains(response, 'test content')
        self.assertEqual(response.context['blog'].pk, self.blog.pk)


class BlogsExportViewTestCase(TestCase):
    fixtures = [
        'auth-fixture.json',
        'users-fixture.json',
        'blogs-fixture.json',
    ]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(
            username='test_user',
            password='n12345678',
            is_staff=True
        )

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_get_blogs_view(self):
        response = self.client.get(reverse('app_blogs:blogs_export'))
        self.assertEqual(response.status_code, 200)
        blogs = Blog.objects.order_by('pk').all()
        expected_data = [
            {
                'pk': blog.pk,
                'author': blog.author.username,
                'content': blog.content,
            }
            for blog in blogs
        ]
        blog_data = response.json()
        self.assertEqual(blog_data['blogs'], expected_data)
