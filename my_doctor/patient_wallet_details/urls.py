from rest_framework import routers
from .api import patient_wallet_detailsViewSet, WalletDetailView
from django.urls import path,include

router = routers.DefaultRouter()
router.register('patient_wallet_details', patient_wallet_detailsViewSet, 'patient_wallet_details')
router.register('wallet_details', WalletDetailView, 'wallet_details')

urlpatterns = [
    path('',include(router.urls)),
    # path('wallet_details/', WalletDetailView.as_view(), name='wallet_details')
]