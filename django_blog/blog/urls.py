from django.urls import path
from .views import RegisterView, HomeView,ChangeView,ChangePassword,ProfileView,CreateView,UpdateView,DetailView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from . import views as out_view
urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('profile/',ProfileView.as_view(),name='profile'),
    path('home/',HomeView.as_view(),name='home'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',out_view.logout_view,name='logout'),
    path('change/',ChangeView.as_view(),name='change'),
    path('change_pass/',ChangePassword.as_view(),name='change-pass'),
    path('post/new/',CreateView.as_view(),name='create'),
    path('post/<int:pk>/update/',UpdateView.as_view(),name='update'),
    path('detail/<int:pk>/',DetailView.as_view(),name='detail'),
    path('post/<int:pk>/delete/',DeleteView.as_view(),name='Delete'),

]

