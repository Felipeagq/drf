from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListAPIView

class MeasureUnitListAPIView(GeneralListAPIView):
    serializer_class = MeasureUnitSerializer # Serializador



class IndicatorListAPIView(GeneralListAPIView):
    serializer_class = IndicatorSerializer



class CategoryProductListAPIView(GeneralListAPIView):
    serializer_class = CategoryProductSerializer
