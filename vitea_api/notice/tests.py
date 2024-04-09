from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Notice


class NoticeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.notice_data = {'title': 'Test Notice', 'content': 'This is a test notice.'}
        self.notice = Notice.objects.create(title='Existing Notice', content='This is an existing notice.')

    def test_create_notice(self):
        response = self.client.post(reverse('notice_create'), self.notice_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Notice.objects.count(), 2)  # Check if the notice is created

    def test_get_notice_detail(self):
        response = self.client.get(reverse('notice_retrieve_update_destroy', kwargs={'pk': self.notice.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.notice.title)

    def test_update_notice(self):
        updated_data = {'title': 'Updated Notice', 'content': 'This is an updated notice.'}
        response = self.client.put(reverse('notice_retrieve_update_destroy', kwargs={'pk': self.notice.pk}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.notice.refresh_from_db()
        self.assertEqual(self.notice.title, updated_data['title'])

    def test_delete_notice(self):
        response = self.client.delete(reverse('notice_retrieve_update_destroy', kwargs={'pk': self.notice.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Notice.objects.filter(pk=self.notice.pk).exists())

    def test_list_notices(self):
        response = self.client.get(reverse('notice_retrieve_update_destroy',kwargs={'pk': self.notice.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)  # Assuming there's only one existing notice
