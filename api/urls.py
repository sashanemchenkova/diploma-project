from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
