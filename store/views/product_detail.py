from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from store.models.product import Product


class ProductDetail(View):
    def get(self, request, id):
        product = get_object_or_404(Product, id=id)
        context = { 'product': product }
        return render(request, 'product_detail.html', context)
    def post(self, request, id):
        product = get_object_or_404(Product, id=id)
        product_id = request.POST.get('product')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                cart[product_id] = quantity + 1
            else:
                cart[product_id] = 1
        else:
            cart = { product_id: 1 }
        request.session['cart'] = cart
        product_count = cart[product_id]
        messages.info(request, f'{product.name} added to cart ({product_count})')
        return redirect('product_detail', id=id)