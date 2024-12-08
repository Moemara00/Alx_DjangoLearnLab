from django.urls import path
from .views import RegisterView, HomeView
from django.contrib.auth.views import LoginView,LogoutView
from . import views as out_view
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('home/',HomeView.as_view(),name='home'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',out_view.logout_view,name='logout'),
]

