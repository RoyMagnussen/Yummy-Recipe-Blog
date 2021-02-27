from accounts.models import Account
from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/home')
        self.assertEqual(response.status_code, 301)

    def test_get_profile_page(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)

    def get_personal_recipes_page(self):
        response = self.client.get('/profile/my_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUser(response, 'blog/personal_recipes.html')

    def test_get_liked_recipes_page(self):
        response = self.client.get('/profile/liked_recipes/')
        self.assertEqual(response.status_code, 302)

    def test_get_user_profile_page(self):
        user = Account.objects.create(
            username='Test User', email='test@test.com', password='Testing@1234')
        response = self.client.get(f'/users/{user.username}/')
        self.assertEqual(response.status_code, 302)
