from django.shortcuts import render
from .models import Product, Category
from .sql_query import SELECT_ALL,SELECT_WHERE
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



def product_list(request):

    list_produc =  SELECT_ALL('catalog_product')
    page = request.GET.get('page',3)
    paginator = Paginator(list_produc, 3)
    try:
        product_lst = paginator.page(page)
    except PageNotAnInteger:
        product_lst = paginator.page(1)
    except EmptyPage:
        product_lst = paginator.page(paginator.num_pages) 
    #product_lst = paginator.get_page(page)
    #paginator = Paginator(list_produc, 1)
    
    context = {'product_list': SELECT_ALL('catalog_product')}
   
    return render(request,'catalog/product_list.html',{'product_list': product_lst})

def category(request, slug):
    #category = Category.objects.get(slug=slug)
    category = SELECT_WHERE(table='catalog_category',slug=slug)
    context = {
        'current_category': category,
        'product_list': Product.objects.filter(category=category),        
    }
    #print("filtre",Product.objects.filter(category=category))
    return render(request, 'catalog/category.html', context)

def product(request,slug):
    #category = Category.objects.get(slug=slug)
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)

