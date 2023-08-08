from django.urls import path
from apps.products.api.views.general_view import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_view import (
    ProductListAPIView,
    ProductRetrieveUpdateDestroyAPIView, ProductListCreateAPIView,
    
)

urlpatterns = [
    path("maesure_unit/", MeasureUnitListAPIView.as_view(), name="measure_unit"),
    path("indicator/", IndicatorListAPIView.as_view(), name="indicator"),
    # path("category_product/", CategoryProductListAPIView.as_view(), name="category_product"),
    # path("products/<int:pk>",ProductRetrieveUpdateDestroyAPIView.as_view(), name="product_list"),
    # path("products/list_create/",ProductListCreateAPIView.as_view(), name="product_list_create"),

]
