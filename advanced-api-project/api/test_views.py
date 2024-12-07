from rest_framework.test import APIRequestFactory, APITestCase, APIClient, force_authenticate
from rest_framework import status
# from django.contrib.auth.models import User
from .models import Book
from django.contrib.auth.models import User
from .models import Author
from .serializers import AuthorSerializer
class TestDetail(APITestCase):


    def setUp(self):
        # Create a user to associate with the user profile
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.first()
        self.url = 'http://127.0.0.1:8000/books/create/'  # URL of the CreateAPIView
        

        self.data = {
            'title': 'GO ALONE',  # Assuming 'user' field expects a user ID
            'publication_year': 2020,
            'author':self.author ,

        }

    def test_create(self):
        
        # self.client.login(username='mohamed', password='123')
        response = self.client.post(self.url,self.data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'GO ALONE')