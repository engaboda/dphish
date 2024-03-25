from django.urls import path
from .views import IpAddressViewSet


urlpatterns = [
    path('ip-info', IpAddressViewSet.as_view({"post": "create"}), name='ip-info'),
]
