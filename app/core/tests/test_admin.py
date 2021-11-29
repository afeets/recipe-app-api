from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse   # helper function to create urls


class AdminSiteTests(TestCase):

    """Setup Function, run before every test is run"""
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password123'
        )
        """client helper function"""
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test1@gmail.com',
            password='password123',
            name='Test User'
        )

    """Check users are listed"""
    def test_users_listed(self):
        """generate url for user list"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    """Check change page renders correctly"""
    def test_user_change_page(self):
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/id
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
