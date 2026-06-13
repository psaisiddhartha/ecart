from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.views import View
from django.conf import settings
from store.models.product import Product
from store.models.orders import Order
from django.contrib import messages

class CheckOut(View):
    def post(self, request):
        customer_id = request.session.get('customer')

        if not customer_id:
            messages.warning(request, "Please login to continue checkout.")
            return redirect('login')
        
        customer = Customer.objects.get(id=customer_id)
        # Validate required profile fields
        if (not customer.name):
            messages.warning(request, "Your name is required")
            return redirect('cart')
        elif (not customer.phone):
            messages.warning(request, "Phone number is required for communication regarding your order")
            return redirect('cart')
        elif (not customer.address):
            messages.warning(request, "Delivery address is required for checkout")
            return redirect('cart')
        else:
            cart = request.session.get('cart', {})
            products = Product.get_products_by_id(list(cart.keys()))

            print(customer, cart, products)

            # Calculate total
            total = sum([
                product.price * cart.get(str(product.id))
                for product in products
            ])

            for product in products:
                Order.objects.create(customer=customer,
                    product=product,
                    price=product.price,
                    address=customer.address,
                    phone=customer.phone,
                    quantity=cart.get(str(product.id)))

            request.session['cart'] = {}

            messages.success(request, "Order placed successfully.")

            return redirect('orders')
