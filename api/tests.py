from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status


class APITest(APITestCase):
    def test_filter_videos_view(self):
        url = reverse('api:get_videos_by_tag')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
