from django.shortcuts import render, get_object_or_404

from store.models import Product, Category


def store(request, category_slug=None):
    # categories = None
    # products = None

    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    return render(request, 'store/store.html', {'products': products, 'product_count': product_count})


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e

    return render(request, 'store/product_detail.html', {'single_product': single_product})

