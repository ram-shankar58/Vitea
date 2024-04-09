from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            campus='Test Campus',
            phone_no='1234567890',
            regno='180101',
            sex='MALE'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.role, 'ST')
        self.assertEqual(user.campus, 'Test Campus')
        self.assertEqual(user.phone_no, '1234567890')
        self.assertEqual(user.regno, '180101')
        self.assertEqual(user.sex, 'MALE')

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='testsuperuser',
            email='testsuper@example.com',
            password='testpass123',
            campus='Test Campus',
            phone_no='1234567890',
            regno='180101',
            sex='MALE'
        )
        self.assertEqual(user.username, 'testsuperuser')
        self.assertEqual(user.email, 'testsuper@example.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.role, 'ST')
        self.assertEqual(user.campus, 'Test Campus')
        self.assertEqual(user.phone_no, '1234567890')
        self.assertEqual(user.regno, '180101')
        self.assertEqual(user.sex, 'MALE')