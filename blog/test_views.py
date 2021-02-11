from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    
    def test_get_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')