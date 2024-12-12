from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name="Login"),
    path('profile/',views.UserView.as_view(),name='profile')
              
              
              
 ]