from rest_framework.viewsets import ModelViewSet

from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from django.http import HttpResponse


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    search_fields = ['title', 'description']
    filter_backends = [DjangoFilterBackend, SearchFilter]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    # при необходимости добавьте параметры фильтрации

    def get_queryset(self):
        product = self.request.query_params.get('products')
        if product:
            return Stock.objects.filter(products__id=product)
        else:
            return self.queryset
        

def test_page_view(request):
    return HttpResponse('This is test_page')
