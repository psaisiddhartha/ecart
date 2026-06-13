from django.shortcuts import render , redirect
from store.models.customer import Customer
from django.views import  View
from store.models.product import Product

class Cart(View):
    def get(self , request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
            cart = request.session['cart']
        ids = list(cart.keys())
        products = Product.get_products_by_id(ids)
        total_items = sum(cart.values())
        customer = None
        customer_id = request.session.get('customer')
        if customer_id:
            customer = Customer.objects.get(id=customer_id)
        context = {
            'products': products,
            'total_items': total_items,
            'customer': customer
        }
        print(products)
        return render(request, 'cart.html', context)

    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        delete = request.POST.get('delete')
        quantity = cart.get(product_id)
        # Remove item completely
        if delete:
            cart.pop(product_id, None)
            request.session['cart'] = cart
            return redirect('cart')

        if quantity:
            quantity = int(quantity)
            if remove:
                if quantity > 1:
                    cart[product_id] = quantity - 1
                else:
                    del cart[product_id]
            else:
                cart[product_id] = quantity + 1
        else:
            cart[product_id] = 1
        request.session['cart'] = cart
        return redirect('cart')