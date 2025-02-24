from rest_framework import viewsets, generics, filters

from users.models import Payments
from users.serializers import PaymentsSerializer, CustomUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer


class PaymentsViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [filters.OrderingFilter]
    filterset_fields = ['course', 'lesson', 'payment_method']
    ordering_fields = ['payment_date']
