from django.urls import path
from apps.products.api.views.general_view import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_view import (
    ProductListAPIView, ProductCreateAPIView,
    ProductRetrieveAPIView, ProductDestroyAPIView,
    ProductUpdateAPIView, ProductListCreateAPIView,
    ProductRetrieveUpdateAPIView
)

urlpatterns = [
    path("maesure_unit/", MeasureUnitListAPIView.as_view(), name="measure_unit"),
    path("indicator/", IndicatorListAPIView.as_view(), name="indicator"),
    path("category_product/", CategoryProductListAPIView.as_view(), name="category_product"),
    path("products/list/",ProductListAPIView.as_view(), name="product_list"),
    path("products/create/",ProductCreateAPIView.as_view(), name="product_create"),
    path("products/retrieve/<int:pk>",ProductRetrieveAPIView.as_view(), name="product_retrieve"),
    path("products/destroy/<int:pk>",ProductDestroyAPIView.as_view(), name="product_destroy"),
    path("products/update/<int:pk>",ProductUpdateAPIView.as_view(), name="product_update"),
    path("products/list_create/",ProductListCreateAPIView.as_view(), name="product_list_create"),
    path("products/read_update/<int:pk>",ProductRetrieveUpdateAPIView.as_view(), name="product_read_update"),
]
