from django.views import View
from django.shortcuts import render, redirect
from store.models.customer import Customer
from django.contrib import messages

class Profile(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        if not customer_id:
            return redirect('login')
        customer = Customer.objects.get(id=customer_id)
        return render(request, 'profile.html', { 'customer': customer })
    
    def post(self, request):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)            
        customer.name = request.POST.get('name', '').strip()
        customer.email = request.POST.get('email')
        if not customer.email:
            messages.error(request, "Email is required.")
            return redirect('profile')
        customer.phone = request.POST.get('phone', '').strip()
        customer.address = request.POST.get('address', '').strip()
        customer.save()
        messages.success(request, "Changes saved")
        return redirect('profile')