from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, StockViewSet, EquipmentViewSet, UserViewSet

router = DefaultRouter()

router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'stocks', StockViewSet, basename='stocks')
router.register(r'equipments', EquipmentViewSet, basename='equipments')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls)),
]
