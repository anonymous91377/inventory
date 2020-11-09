from django.db import models

# Create your models here.

class Supplier(models.Model):
    name=models.CharField(max_length=64)
    address=models.TextField(max_length=128)
    contact_no=models.IntegerField(default=91)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id']
    def __str__(self):
        return self.name

class Product_detail(models.Model):
    product_quantity=models.IntegerField(default=0)
    product_price=models.FloatField(default=0.0)
    product_gst=models.FloatField(default=0)
    purchase_product=models.ForeignKey('Purchase_product',on_delete=models.CASCADE,related_name='Product_detail')
    supplier=models.ForeignKey('Supplier',on_delete=models.CASCADE,related_name='Product_detail')
    created_at=models.DateTimeField(auto_now_add=True)
    modifies_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s | %s | %s | %s | %s' %(self.product_quantity,self.product_price,self.product_gst,self.purchase_product.product_name,self.supplier.name)


class Purchase_product(models.Model):
    product_name=models.CharField(max_length=64,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.product_name

class Stock(models.Model):
    product_name=models.CharField(max_length=64)
    quantity=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-id']
    def __str__(self):
        return '%s | %s' %(self.product_name,self.quantity)

class Purchase_return(models.Model):
    product=models.ForeignKey('Purchase_product',models.SET_NULL,null=True,related_name='purchase_return')
    quantity=models.IntegerField(default=0)
    price=models.FloatField(default=0.0)
    gst=models.FloatField(default=0)
    supplier=models.ForeignKey('Supplier',models.SET_NULL,null=True,related_name='purchase_return')
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-id']

    def __str__(self):
        return '%s | %s' %(self.product.product_name,self.supplier.name)
    
