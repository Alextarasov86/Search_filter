from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'articles', ArticlesViewSet, basename='articles')
router.register(r'comments', CommentsViewSet, basename='comments')
router.register(r'categories', CategoriesViewSet, basename='categories')

urlpatterns = [
    path('', include(router.urls)),
]