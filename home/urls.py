from django.urls import path
from home.views import home_page
from home.views import shop_page
from home.views import single_product
from home.views import checkout
from home.views import cart

urlpatterns = [
    path("", home_page, name="home_page"),
    path("shop_page", shop_page, name="shop_page"),
    path("single_product", single_product , name="single_product"),
    path("checkout", checkout , name="checkout"),
    path("cart", cart , name="cart"),
]
