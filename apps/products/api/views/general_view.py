from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListAPIView
from rest_framework import viewsets

class MeasureUnitListAPIView(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer # Serializador
    queryset = serializer_class.Meta.model.objects.filter(state = True)



class IndicatorListAPIView(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)



class CategoryProductListAPIView(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)
    

