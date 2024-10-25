from django import forms
from service_objects.services import Service
from rest_framework import status
from service_objects.errors import ValidationError
from api.models import Transaction


class CreateTransactionService(Service):
    user = forms.IntegerField()
    amount = forms.DecimalField()
    type = forms.CharField()
    category = forms.CharField()

    def process(self):
        self.result = self._create_transaction
        return self

    @property
    def _create_transaction(self):
        return Transaction.objects.create(
            user_id=self.cleaned_data['user'],
            amount=self.check_positive_number(self.cleaned_data['amount']),
            type=self.cleaned_data['type'],
            category=self.cleaned_data['category']
        )

    def check_positive_number(self, num):
        if num <= 0:
            raise ValidationError(
                message='Сумма транзакции должна быть больше нуля',
                response_status=status.HTTP_400_BAD_REQUEST
            )
        return self.cleaned_data['amount']
