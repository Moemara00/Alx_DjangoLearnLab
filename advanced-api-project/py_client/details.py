from rest_framework.test import force_authenticate, APIRequestFactory
from django.conf import settings
from api.views import DetailView
from django.contrib.auth.models import User

factory = APIRequestFactory()
user = User.objects.get(username='mohamed')
view = DetailView.as_view()

# Make an authenticated request to the view...
request = factory.get('/accounts/django-superstars/')
force_authenticate(request, user=user)
response = view(request)



