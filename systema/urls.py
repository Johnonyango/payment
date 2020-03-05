from django.urls import path, include
from . import views
from rest_framework import routers
from .models import MpesaPayment

router = routers.DefaultRouter()
router.register(r'MpesaPayment', views.MpesaPaymentViewSet)



urlpatterns = [
    path('', views.accessToken, name = 'get_mpesa_access_token'),
    path('online/lipa', views.lipa_na_mpesa_online, name='lipa_na_mpesa'),

    path('c2b/register', views.register_urls, name="register_mpesa_validation"),
    path('c2b/confirmation', views.confirmation, name="confirmation"),
    path('c2b/validation', views.validation, name="validation"),
    path('c2b/callback', views.call_back, name="call_back"),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls))


]
