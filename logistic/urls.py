from django.urls import path
from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet

from .views import test_page_view


router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = [
    path('test_page/', test_page_view)
] + router.urls
