from django.shortcuts import render
from . models import Product
from . models import Category

# Create your views here.

def home_view(request):
    return render(request,'eapp/home.html')

def create_product_view(request):
    if request.method == 'POST':
        product_title1 = request.POST.get('product_title','')
        image1 = request.POST.get('image')
        category1 = request.POST.get('category','')
        price1 = request.POST.get('price','')
        discription1 = request.POST.get('discription','')
        created_at1 = request.POST.get('created_at','')
        updated_at1 = request.POST.get('updated_at','')
        Product.objects.create(product_title=product_title1, image=image1, category=category1, price=price1, discription=discription1, created_at=created_at1, updated_at=updated_at1)
    return render(request,'eapp/create_product.html')




def products_view(request):
    products = Product.objects.all()
    return render(request,'eapp/products.html',{'product':products})

def categories_view(request):
    categories= Category.objects.all()
    return render(request,'eapp/create_product.html',{'categories':categories})