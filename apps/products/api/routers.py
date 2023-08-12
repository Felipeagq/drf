from rest_framework.routers import DefaultRouter
from apps.products.api.views.product_view import ProductViewSet
from apps.products.api.views.general_view import (
    MeasureUnitListAPIView,CategoryProductListAPIView,IndicatorListAPIView
)

router = DefaultRouter()
router.register(r"products",ProductViewSet,basename="products")
router.register(r"measure-unit",MeasureUnitListAPIView,basename="measure-unit")
router.register(r"indicators",CategoryProductListAPIView,basename="indicators")
router.register(r"category",IndicatorListAPIView,basename="category")

urlpatterns = router.urls