from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,UsersPosts
router = DefaultRouter()
router.register('posts',PostViewSet)
router.register('comments',CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/',UsersPosts.as_view(),name='feed-posts')
]