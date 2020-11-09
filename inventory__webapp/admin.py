from django.contrib import admin
from .models import Purchase_product,Supplier,Product_detail,Stock,Purchase_return
# Register your models here.
admin.site.register(Purchase_product)
admin.site.register(Supplier)
admin.site.register(Product_detail)
admin.site.register(Stock)
admin.site.register(Purchase_return)