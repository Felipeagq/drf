from apps.products.models import Product
from apps.products.api.serializers.general_serializer import MeasureUnitSerializer, CategoryProductSerializer
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()
    
    class Meta:
        model = Product
        exclude = ("state",)
    
    def to_representation(self, instance):
        return {
            "id": instance.id,
            "description":instance.description,
            # "image":instance.image,
            "measure_unit": instance.measure_unit.description,
            "category_product":instance.category_product.description
        }