from rest_framework.test import APIRequestFactory , force_authenticate
from django.conf import settings
from api.views import DetailView
User = settings.AUTH_USER_MODEL 
factory = APIRequestFactory()
request = factory.get('http://127.0.0.1:8000/books/2/')
user = User.objects.get(username='mohamed')
view = DetailView.as_view()
response = force_authenticate(request,user=user)