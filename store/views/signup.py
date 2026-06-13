import random

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.utils import timezone
from store.models.customer import Customer
from store.utils import send_otp_email


class Signup(View):

    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        email = request.POST.get("email")
        request.session['signup_email'] = email  # store temporarily

        if not email:
            messages.error(request, "Email is required")
            return redirect("signup")
        
        if Customer.objects.filter(email=email).exists():
            messages.error(request, 'Account already exists with this email address')
            return redirect("signup.html")
        
        current_time = timezone.now().timestamp()

        existing_otp = request.session.get("otp")
        otp_email = request.session.get("otp_email")
        otp_purpose = request.session.get("otp_purpose")
        otp_created_at = request.session.get("otp_created_at")

        # Reuse OTP if it is still valid (5 minutes)
        if (
            existing_otp
            and otp_email == email
            and otp_purpose == "signup"
            and otp_created_at
            and (current_time - otp_created_at) < 300
        ):
            otp = existing_otp

            # Print OTP
            print("=" * 40)
            print(f"Signup OTP for {email}: {otp}")
            print("=" * 40)
        
        else:
            # Generate OTP
            otp = str(random.randint(100000, 999999))

            # Print OTP in terminal (development only)
            print("=" * 40)
            print(f"Signup OTP for {email}: {otp}")
            print("=" * 40)

            # Send email
            send_otp_email(email, otp)

            request.session["otp"] = otp
            request.session["otp_email"] = email
            request.session["otp_purpose"] = "signup"
            request.session["otp_created_at"] = current_time

        request.session["signup_data"] = {
                "email": email
            }

        # Display mesage
        messages.success(request, f"OTP sent to '{email}'")

        return redirect("verify_otp")
