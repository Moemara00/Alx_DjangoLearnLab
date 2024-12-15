from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,UsersPosts,LikingView,UnLikingView
router = DefaultRouter()
router.register('posts',PostViewSet)
router.register('comments',CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/',UsersPosts.as_view(),name='feed-posts'),
    path('<int:pk>/like/',LikingView.as_view(),name='like'),
    path('<int:pk>/unlike/',UnLikingView.as_view(),name='unlike'),
]