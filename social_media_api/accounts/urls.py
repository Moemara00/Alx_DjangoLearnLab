from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name="Login"),
    path('profile/',views.UserView.as_view(),name='profile'),
    path('log/',obtain_auth_token),
    path("follow/<str:username>/",views.FollowView.as_view(),name='follow'),
    path("unfollow/<str:username>/",views.UnFollowView.as_view(),name='unfollow')

              
 ]