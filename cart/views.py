from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from onlineshop.models import ShopList
from .cart import Cart
from .forms import CartAddProductForm
from onlineshop.models import Category

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ShopList, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(ShopList, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    cats = Category.objects.all()
    return render(request, 'cart/detail.html', {'cart': cart, 'cats': cats, 'title': 'Корзина'})
