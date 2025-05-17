from api.models import Transaction
from api.serializers.user.list import UserSerializer
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Transaction
        fields = ("id", "user", "amount", "date", "type", "category")
