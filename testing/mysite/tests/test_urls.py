from http import HTTPStatus

from django.test import Client
from django.test import TestCase
from django.test.utils import override_settings
from django.urls import reverse


@override_settings(ROOT_URLCONF='mysite.tests.urls')
class TestURLs(TestCase):
    def setUp(self):
        self.client = Client()

    def test_myapp_index(self):
        response = self.client.get(reverse('myapp:index'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
