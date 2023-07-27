from django.db import models

# Create your models here.
from apps.base.models import BaseModel

class MeasureUnit(BaseModel):
    """Model definition for MeasureUnit."""
    # TODO: Define fields here
    description = models.CharField(max_length=50,blank=False, null=False,unique=True)
    class Meta:
        """Meta definition for MeasureUnit."""
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'
    def __str__(self):
        """Unicode representation of MeasureUnit."""
        return self.description


class CategoryProduct(BaseModel):
    """Model definition for CategoryProduct."""
    # TODO: Define fields here
    description = models.CharField(max_length=50)
    class Meta:
        """Meta definition for CategoryProduct."""
        verbose_name = 'CategoryProduct'
        verbose_name_plural = 'CategoryProducts'
    def __str__(self):
        """Unicode representation of CategoryProduct."""
        return self.description



class Indicator(BaseModel):
    """Model definition for Indicator."""
    # TODO: Define fields here
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=False,verbose_name="Category Products")
    discount_value = models.PositiveSmallIntegerField(default=0)
    class Meta:
        """Meta definition for Indicator."""
        verbose_name = 'Indicator'
        verbose_name_plural = 'Indicators'
    def __str__(self):
        """Unicode representation of Indicator."""
        return f"Oferta de la categoria {self.category_product} es de {self.discount_value}"



class Product(BaseModel):
    """Model definition for Product."""
    # TODO: Define fields here
    product = models.CharField("Product name", max_length=150, unique=True, blank=False, null=False)
    description = models.TextField("Product description",blank=False, null=False)
    image = models.ImageField("Product image", upload_to="products/", blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, null=True,verbose_name="Measure Unit")
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True,verbose_name="Category Product")
    class Meta:
        """Meta definition for Product."""
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    def __str__(self):
        """Unicode representation of Product."""
        return self.product
