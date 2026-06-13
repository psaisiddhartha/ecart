from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View

class Logout(View):
    def get(self, request):
        request.session.pop('customer', None)
        request.session.pop('customer_name', None)
        request.session.pop('cart', None)
        return redirect('homepage')