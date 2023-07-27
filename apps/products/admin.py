from django.contrib import admin
from apps.products.models import *

# Register your models here.
class AdminView(admin.ModelAdmin):
    list_display = ("id","description")

admin.site.register(MeasureUnit,AdminView)
admin.site.register(CategoryProduct,AdminView)
admin.site.register(Indicator)
admin.site.register(Product)