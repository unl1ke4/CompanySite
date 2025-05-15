from django.test import TestCase
from django.urls import reverse

class IndexPageTests(TestCase):
    def test_index_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    def test_index_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'index.html')