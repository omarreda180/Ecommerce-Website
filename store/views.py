from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def product_all(request):
    products = Product.products.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)


def product_details(request, product_details):
    product = get_object_or_404(Product, slug=product_details, in_stock=True)
    context = {
        'product': product,
    }
    return render(request, 'products/single.html', context)


def category_list(request, category_list=None):
    category = None
    if category_list is not None:
        category = get_object_or_404(Category, slug=category_list)
        products = Product.products.filter(category=category)
    else:
        products = Product.products.all()

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'products/store.html', context)
