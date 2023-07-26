from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from rest_framework import generics

class MeasureUnitListAPIView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer # Serializador
    def get_queryset(self):
        return MeasureUnit.objects.filter(state = True) # Modelo


class IndicatorListAPIView(generics.ListAPIView):
    serializer_class = IndicatorSerializer
    def get_queryset(self):
        return Indicator.objects.filter(state = True)


class CategoryProductListAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer
    def get_queryset(self):
        return CategoryProduct.objects.filter(state = True)