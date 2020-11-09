from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from .models import Purchase_product,Supplier,Product_detail,Stock,Purchase_return
from django.db.models import Q
from django.core.mail import send_mail
# Create your views here.
def dashboard(request):
    return render(request,'inventory__webapp/dashboard.html',context={})

# create purchase record
def purchase_product(request):
    data=dict()
    if request.method=="POST":
        product_name=request.POST.get('product_name')
        product_price=request.POST.get('product_price')
        product_quantity=request.POST.get('product_quantity')
        product_gst=request.POST.get('product_gst')
        supplier=request.POST.get('supplier')
        address=request.POST.get('address')
        contact_no=request.POST.get('contact_no')
     
        # create supplier
        if__supplier__exist(supplier,address,contact_no)
        # create global variable 
        
        # create product 
        if__product__exist(product_name)
        # create gobal variable
        purchase__product__obj=Purchase_product()

        # add quantity
        add__product__details(product_quantity,product_price,product_gst,product_name,supplier,contact_no) 
        return JsonResponse({'status':'ok'})
    else:
        print('else')
        data['purchase_product_form']=render_to_string('inventory__webapp/purchase_product_form.html',context={},request=request)
        return JsonResponse(data)

# create supplier
def if__supplier__exist(supplier,address,contact_no):
    supplier__obj=Supplier()
    # check supplier exist or not
    # Supplier obj saved if new 
    supplier_exist=Supplier.objects.filter(contact_no=contact_no)
    if supplier_exist.count()==0:
        print('supplier saved')
        supplier__obj=Supplier(name=supplier,address=address,contact_no=contact_no)
        supplier__obj.save()

    else:
        print(' supplier exist')
        
# create product
def if__product__exist(product_name):
    # check product  exist or not
    # Purchase product saved if new
    purchase_product__exist=Purchase_product.objects.filter(product_name=product_name) 
    if purchase_product__exist.count()==0:
        print('product saved')
        purchase__product__obj=Purchase_product(product_name=product_name)
        purchase__product__obj.save()

    else:
        print('product exist')
        
# create quantity
def add__product__details(product_quantity,product_price,product_gst,product_name,supplier,contact_no):
    supplier__obj=Supplier.objects.get(contact_no=contact_no)
    purchase__product__obj=Purchase_product.objects.get(product_name=product_name)
    product__detail__obj=Product_detail(product_quantity=product_quantity,product_price=product_price,product_gst=product_gst,purchase_product=purchase__product__obj,supplier=supplier__obj)
    product__detail__obj.save()

       
# show all product records
def show_purchase_record(request):
    data=dict()
    records=dict()
    list=[]
    import datetime
    pd_obj=Product_detail.objects.all()
    for read in pd_obj:
        print(read)
        p_obj=Purchase_product.objects.get(pk=read.purchase_product.pk)  
        s_obj=Supplier.objects.get(pk=read.supplier.pk)
        records['product_quantity']=read.product_quantity
        records['product_name']=p_obj.product_name
        records['product_price']=read.product_price
        records['product_gst']=read.product_gst
        records['name']=s_obj.name
        records['address']=s_obj.address
        records['contact_no']=s_obj.contact_no
        records['pk']=read.pk
        records['p_pk']=p_obj.pk
        records['s_pk']=s_obj.pk
        datetime=read.created_at
        date=datetime.date()
        records['created_at']= str(date.year)+"-"+str(date.month)+"-"+str(date.day)
        list.append(records.copy())
    print(len(list))
            
    data['purchase_render']=render_to_string('inventory__webapp/purchase.html',context={'data':list},request=request)
    return JsonResponse(data)

# edit Product records
def edit_purchase_product(request,pk):
    data=dict()
    if request.method=='POST':
        product_name=request.POST.get('product_name')
        product_price=request.POST.get('product_price')
        product_quantity=request.POST.get('product_quantity')
        product_gst=request.POST.get('product_gst')
        supplier_name=request.POST.get('supplier')
        contact_no=request.POST.get('contact_no')
        address=request.POST.get('address')

        pd_oj=Product_detail.objects.get(pk=pk)
        s_pk=pd_oj.supplier.pk
        # call edit_supplier_name to update supllier name
        s_pk=edit_supplier_name(supplier_name,contact_no,address,s_pk)

        # call edit_purchase_product_name update product name
        p_pk=edit_purchase_product_name(product_name)

        # call edit_product_detail function for editing data 
        edit_product_detail(pk,product_quantity,product_price,product_gst,p_pk,s_pk)

        return JsonResponse({'status':product_name})
        
    else:
        # reading value for displaying in for for editing purpose 
        pd_obj=Product_detail.objects.get(pk=pk)
        quantity=pd_obj.product_quantity
        price=pd_obj.product_price
        gst=pd_obj.product_gst
        s_pk=request.GET.get('s_pk')
        p_pk=request.GET.get('p_pk')
        # getting purchase_prodcut model objects
        purchase_product_obj=Purchase_product.objects.get(pk=p_pk)
        # getting Sipllier objects
        supplier_obj=Supplier.objects.get(pk=s_pk)
        product_name=purchase_product_obj.product_name

        print(product_name)
        supplier_name=supplier_obj.name
        supplier_address=supplier_obj.address
        supplier_contact=supplier_obj.contact_no
        data['edit_purchase_product_form']=render_to_string('inventory__webapp/edit_purchase_product_modal_form.html',
        context={'pk':pk},request=request)
        data['status']='ok'
        data['context']={'quantity':quantity,'price':price,'gst':gst,'product_name':product_name,'supplier_name':supplier_name,
        'pk':pk,'supplier_address':supplier_address,'supplier_contact':supplier_contact}
        return JsonResponse (data)

# edit product detlais models data

def edit_product_detail(pk,product_quantity,product_price,product_gst,p_pk,s_pk):
    print(type(s_pk))
    print('product details data updated')
    product_detail_obj=Product_detail.objects.get(pk=pk)
    product_detail_obj.product_price=product_price
    product_detail_obj.product_quantity=product_quantity
    product_detail_obj.product_gst=product_gst
    product_detail_obj.purchase_product=p_pk
    product_detail_obj.supplier=s_pk
    product_detail_obj.save()

    # delete product name who is not pointing to its details 
    # delete_product_name()


# edit supplier name
def edit_supplier_name(supplier_name,contact_no,address,s_pk):
    print('enter into supplier')
    print(contact_no)
    s_obj=Supplier.objects.get(pk=s_pk)
    s_obj.address=address
    s_obj.name=supplier_name
    s_obj.contact_no=contact_no
    s_obj.save()
    return s_obj


# edit product name

def edit_purchase_product_name(product_name):
    print('enter into product')
    if Purchase_product.objects.filter(product_name=product_name).exists():
        p_obj=Purchase_product.objects.get(product_name=product_name)
        print('pk',p_obj.pk,'name',p_obj.product_name)
        return p_obj
    else:
        print('add one more product')
        p_obj=Purchase_product(product_name=product_name)
        p_obj.save()
        return p_obj

# Working on Stock module
from django.db.models import Sum
def display__product__name__with__some__of__its__quantity(request):
    Stock.objects.all().delete()
    data=dict() 
    result=dict()
    list=[]
    p_obj=Purchase_product.objects.all()
    for read in p_obj:
        # store in Stock model
        try:
            length=read.Product_detail
            product_name=read.product_name
            quantity=read.Product_detail.aggregate(Sum('product_quantity'))
            stock__obj=Stock(product_name=product_name,quantity=quantity['product_quantity__sum'])
            stock__obj.save()
        except Exception as error:
            product_name=read.product_name
            quantity=0  
            stock__obj=Stock(product_name=product_name,quantity=quantity)
            stock__obj.save()
            print(error)
            
    # show all data 
    stock__obj=Stock.objects.all()
    for read in stock__obj:
        result['product_name']=read.product_name
        result['quantity']=read.quantity
        list.append(result.copy())
    data['stock']=render_to_string('inventory__webapp/stock.html',context={'data':list},request=request)
    data['status']='ok'
    return JsonResponse(data)

# Purchase Return body

def Purchase__return__container(request):
    data=dict()
    result=dict()
    list=[]
    pr__obj=Purchase_return.objects.all()
    for read in pr__obj:
        result['product_name']=read.product.product_name
        result['quantity']=read.quantity
        result['price']=read.price
        result['gst']=read.gst
        result['supplier']=read.supplier.name
        result['address']=read.supplier.address
        result['contact_no']=read.supplier.contact_no
        datetime=read.created_at
        date=datetime.date()
        result['created_at']= str(date.year)+"-"+str(date.month)+"-"+str(date.day)
        list.append(result.copy())
    data['purchasereturn']=render_to_string('inventory__webapp/purchase__return.html',context={'data':list},request=request)
    data['status']='ok'
    return JsonResponse(data)

def Purchase__return(request):
    data=dict()
    if request.method=='POST':
        # read all data from form
        product_name=request.POST.get('product_name')
        product_price=request.POST.get('product_price')
        product_gst=request.POST.get('product_gst')
        product_quantity=request.POST.get('product_quantity')
        supplier=request.POST.get('supplier')
        address=request.POST.get('address')
        contact_no=request.POST.get('contact_no')
        try:
            # call edit_purchase_product_name if exist retur obj else add product then return obj
            p_obj=edit_purchase_product_name(product_name)

            # call edit__supplier__name if exist the return obj else add supplier with its contact_no return obj
            s_obj=edit__supplier__name(supplier,contact_no,address)

            pr_obj=Purchase_return(product=p_obj,supplier=s_obj,price=product_price,gst=product_gst,
            quantity=product_quantity
            )
            pr_obj.save()
            print('inserted successfully')
        except Exception as error:
            print("error is -->",error)

        data['status']='saved'
        return JsonResponse(data)
    else:
        print('else')
        data['purchase__return__modal']=render_to_string('inventory__webapp/purchase__return__modal.html',context={},request=request)
        data['status']='modal'
        return JsonResponse(data)

def edit__supplier__name(supplier,contact_no,address):
    exist__obj=Supplier.objects.filter(Q(name=supplier) & Q(contact_no=contact_no))
    if exist__obj:
        print('supplier exist')
        exist__obj=Supplier.objects.get(name=supplier,contact_no=contact_no)
        return exist__obj
    else:
        s_obj=Supplier(name=supplier,address=address,contact_no=contact_no)
        s_obj.save()
        print('save ad retur ojj')
        return s_obj