from django.shortcuts import render
from .models import Product, Category
from .sql_query import SELECT_ALL,SELECT_WHERE

def product_list(request):
	context = {
        'product_list': SELECT_ALL('catalog_product')
    }
	return render(request,'catalog/product_list.html',context)

def category(request, slug):
    #category = Category.objects.get(slug=slug)
    category = SELECT_WHERE(slug=slug)

    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),
    }
    return render(request, 'catalog/category.html', context)

def product(request,slug):
    #category = Category.objects.get(slug=slug)
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)

