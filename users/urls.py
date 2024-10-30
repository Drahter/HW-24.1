from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.apps import UsersConfig
from users.views import PaymentListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payments/', PaymentListAPIView.as_view(), name='payment-list'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
