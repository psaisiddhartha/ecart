from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from django.contrib import messages
from store.models.customer import Customer


class VerifyOTP(View):

    def get(self, request):

        purpose = request.session.get("otp_purpose")

        if purpose == "login":
            email = request.session.get("otp_email")

        elif purpose == "signup":
            data = request.session.get("signup_data")
            if not data:
                return redirect("signup")
            email = data.get("email")

        else:
            return redirect("login")

        return render(request, "verify_otp.html", {"email": email})

    def post(self, request):

        entered_otp = request.POST.get("otp")
        purpose = request.session.get("otp_purpose")
        session_otp = request.session.get("otp")

        # ❌ invalid session
        if not session_otp:
            messages.error(request, "Session expired. Please request a new OTP.")
            return redirect("login")

        otp_created_at = request.session.get("otp_created_at")

        if (
            not otp_created_at
            or timezone.now().timestamp() - otp_created_at > 300
        ):
            request.session.pop("otp", None)
            request.session.pop("otp_email", None)
            request.session.pop("otp_purpose", None)
            request.session.pop("otp_created_at", None)

            messages.error(request, "OTP has expired. Please request a new OTP.")

        # -----------------------
        # SIGNUP FLOW
        # -----------------------
        if purpose == "signup":

            signup_data = request.session.get("signup_data")

            if entered_otp != session_otp:
                messages.error(request, "Invalid OTP.")
                return redirect("verify_otp")

            # create user (EMAIL ONLY)
            customer = Customer(
                email=signup_data.get("email")
            )
            customer.register()

            # Clear session
            request.session.pop("signup_data", None)
            request.session.pop("otp", None)
            request.session.pop("otp_email", None)
            request.session.pop("otp_purpose", None)
            request.session.pop("otp_created_at", None)

            messages.success(request, "Account created successfully!")

            return redirect("homepage")

        # -----------------------
        # LOGIN FLOW
        # -----------------------
        elif purpose == "login":

            email = request.session.get("otp_email")

            if entered_otp != session_otp:
                messages.error(request, "Invalid OTP.")
                return redirect("verify_otp")

            customer = Customer.get_customer_by_email(email)

            if not customer:
                messages.error(request, "User not found.")
                return redirect("login")

            # login user
            request.session["customer"] = customer.id
            request.session["customer_name"] = customer.name or ""

            # clear session
            request.session.pop("otp_email", None)
            request.session.pop("otp", None)
            request.session.pop("otp_purpose", None)
            request.session.pop("otp_created_at", None)

            messages.success(request, f"Hi {customer.name}!")

            return redirect("homepage")

        return redirect("login")