from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib import messages
from store.models.customer import Customer
from store.utils import send_otp_email

import random


class Login(View):
    return_url = None

    def get(self, request):
        request.session["return_url"] = request.GET.get("return_url")
        return render(request, "login.html")

    def post(self, request):
        email = request.POST.get("email")

        customer = Customer.get_customer_by_email(email)

        if not customer:
            messages.error(request, "No account found with this email.")
            return redirect("login")
        
        current_time = timezone.now().timestamp()

        existing_otp = request.session.get("otp")
        otp_email = request.session.get("otp_email")
        otp_purpose = request.session.get("otp_purpose")
        otp_created_at = request.session.get("otp_created_at")

        # Reuse OTP if it exists and is not older than 5 minutes
        if (
            existing_otp
            and otp_email == email
            and otp_purpose == "login"
            and otp_created_at
            and (current_time - otp_created_at) < 300  # 5 minutes
        ):
            otp = existing_otp
            print('=' * 40)
            print(f"Reusing existing OTP for {email}: {otp}")
            print('=' * 40)
        else:
            # Generate OTP
            otp = str(random.randint(100000, 999999))

            # Print OTP in terminal (development only)
            print("=" * 40)
            print(f"Login OTP for {email}: {otp}")
            print("=" * 40)
            
            # Store email in session
            request.session["otp"] = otp
            request.session["otp_email"] = email
            request.session["otp_purpose"] = "login"
            request.session["otp_created_at"] = current_time

            #Send email
            send_otp_email(email, otp)
        
        # Show message
        messages.success( request, f"OTP sent to '{email}'")
        
        return redirect("verify_otp")