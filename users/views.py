from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter

from users.models import Payment
from users.serializsers import PaymentSerializer


# Create your views here.
class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['payment_method', 'course', 'lesson']
    ordering_fields = ['date']
