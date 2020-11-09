
from django.urls import path
from inventory__webapp import views
urlpatterns = [
  path('dashboard/',views.dashboard,name='dashboard'),
  path('show_purchase_record/',views.show_purchase_record,name='show_purchase_record'),
  path('purchase_product/',views.purchase_product,name='purchase_product'),
  path('edit_purchase_product/<int:pk>/',views.edit_purchase_product,name='edit_purchase_product'),
  path('stock/',views.display__product__name__with__some__of__its__quantity,name='stock'),
  path('PurchaseReturnContainer/',views.Purchase__return__container,name='PurchaseReturnContainer'),
  path('PurchaseReturn/',views.Purchase__return,name='PurchaseReturn')

]
