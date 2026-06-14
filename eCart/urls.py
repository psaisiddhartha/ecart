from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url="store", permanent=False)),
    path('store/' , include('store.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
