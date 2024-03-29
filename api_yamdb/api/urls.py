from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import SignUp, UsersViewSet, get_token

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet)

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register(r'users', UsersViewSet, basename='users')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews',
                   ReviewViewSet, basename='reviews')
v1_router.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)'
                   r'/comments', CommentViewSet, basename='comments')
v1_router.register(r'categories', CategoryViewSet, basename='category')
v1_router.register(r'genres', GenreViewSet, basename='genres')
v1_router.register(r'titles', TitleViewSet, basename='title')

urlpatterns = [
    path('v1/auth/token/', get_token, name='get_token'),
    path('v1/auth/signup/', SignUp.as_view(), name='signup'),
    path('v1/', include(v1_router.urls))
]
