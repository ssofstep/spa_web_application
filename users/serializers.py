from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
