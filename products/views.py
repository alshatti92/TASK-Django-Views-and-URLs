from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
# def get_home(request):
#     return HttpResponse("<h1> Ready to Loose Money !? </h1>")


# def get_product(request, product_id):
#     product = Product.objects.get(id=product_id)
#     return HttpResponse(f""" you will loose money for:
#     <p> {product.id} </p>
#     <h1> {product.name} </h1>
#     <p> {product.price} </p>""")


def get_home(request):
    return render(request, "home.html")


def get_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        "product": {
            "name": product.name,
            "description": product.description,
            "price": product.price,
        }
    }
    return render(request, "product-detail.html", context)


def get_products(request):
    products = Product.objects.all()

    new_products = []
    for product in products:
        new_products.apppend(
            {
                "name": product.name,
                "price": product.price,
            }
        )

    context = {"product": new_products}

    return render(request, "product-list.html", context)
