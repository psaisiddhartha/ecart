from django.db import  models
from django.utils import timezone
from datetime import timedelta

class Customer(models.Model):
    name = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    email = models.EmailField()
    address = models.CharField(max_length=100, default="")
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        return Customer.objects.filter(email = self.email).exists()

    def set_otp(self, otp):
        self.otp = otp
        self.otp_created_at = timezone.now()
        self.save()

    def clear_otp(self):
        self.otp = None
        self.otp_created_at = None
        self.save()

    def is_otp_valid(self, entered_otp):
        if not self.otp or not self.otp_created_at:
            return False

        expiry_time = self.otp_created_at + timedelta(minutes=5)

        if timezone.now() > expiry_time:
            return False

        return self.otp == entered_otp


