from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.signup import Signup
from .views.login import Login
from .views.verify_otp import VerifyOTP
from .views.profile import Profile
from .views.logout import Logout
from .views.cart import Cart
from .views.search import Search
from .views.checkout import CheckOut
from .views.orders import OrderView
from .views.product_detail import ProductDetail
from .middlewares.auth import  auth_middleware


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('/search', Search.as_view(), name='search'),
    path('/product/<int:id>/', ProductDetail.as_view(), name='product_detail'),
    path('/signup', Signup.as_view(), name='signup'),
    path('/login', Login.as_view(), name='login'),
    path('/verify_otp', VerifyOTP.as_view(), name='verify_otp'),
    path('/profile', Profile.as_view(), name='profile'),
    path('/logout', Logout.as_view(), name='logout'),
    path('/cart', Cart.as_view() , name='cart'),
    path('/checkout', CheckOut.as_view() , name='checkout'),
    path('/orders', auth_middleware(OrderView.as_view()), name='orders'),
]
