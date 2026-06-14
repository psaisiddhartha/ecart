from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.customer import Customer
from django.views import  View

class Logout(View):
    def get(self, request):
        request.session.pop('customer', None)
        request.session.pop('customer_name', None)
        request.session.pop('cart', None)
        return redirect('homepage')