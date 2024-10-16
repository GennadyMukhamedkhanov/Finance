from django import forms
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.services import Service

from api.models import Transaction


class DeleteTransactionService(Service):
    id = forms.IntegerField()

    def process(self):
        self.result = self._delete_transaction
        return self

    @property
    def _delete_transaction(self):
        obj = self.transaction_presence()
        obj.delete()
        return True

    def transaction_presence(self):
        transaction = Transaction.objects.filter(id=self.cleaned_data['id'])
        if not transaction.exists():
            raise ValidationError(
                message='Транзакции с таким id не существует.',
                response_status=status.HTTP_400_BAD_REQUEST
            )

        return transaction.first()