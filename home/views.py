from django.shortcuts import render

def home_page(request):
    return render(request, "home.html", {})

def shop_page(request):
    return render(request, "shop_page.html", {})

def single_product(request):
    return render(request, "single_product.html", {})

def checkout(request):
    return render(request, "checkout.html", {})

def cart(request):
    return render(request, "cart.html", {})



