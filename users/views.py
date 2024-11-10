from rest_framework.generics import CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payment, User
from users.serializsers import PaymentSerializer, UserSerializer


# Create your views here.
class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method', 'course', 'lesson']
    ordering_fields = ['date']


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
