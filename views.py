from django.shortcuts import render, redirect,get_object_or_404
from .models import Product

def product_form(request):
    if request.method == "POST":
        product_id = request.POST["productId"]
        name = request.POST["name"]
        description = request.POST["description"]
        category = request.POST["category"]
        price = request.POST["price"]
        stock_quantity = request.POST["stockQuantity"]
        ratings = request.POST.get("ratings", None)
        if ratings == "":  # Convert empty string to None
            ratings = None
        else:
            ratings = float(ratings)

        # Check if product already exists
        if Product.objects.filter(productId=product_id).exists():
            return render(request, "product_form.html", {"error": "Product ID already exists!"})

        # Save product to MongoDB
        Product.objects.create(
            productId=product_id,
            name=name,
            description=description,
            category=category,
            price=price,
            stockQuantity=stock_quantity,
            ratings=ratings
        )
        return redirect("product_list")

    return render(request, "product_form.html")

def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, productId=product_id)
    product.delete()
    return redirect("product_list")

