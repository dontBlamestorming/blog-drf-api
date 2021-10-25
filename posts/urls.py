from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()

router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'category', views.CategoryViewSet, basename='category')

urlpatterns = router.urls
