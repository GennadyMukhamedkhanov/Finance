from service_objects.services import Service
from api.models import Transaction
from django import forms
from service_objects.errors import ValidationError
from rest_framework import status


class GetTransactionService(Service):
    id = forms.IntegerField()

    def process(self):
        self.result = self._search_transaction
        return self

    @property
    def _search_transaction(self):
        user = Transaction.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise ValidationError(
                message='Транзакции с таким id не существует.',
                response_status=status.HTTP_404_NOT_FOUND
            )
        return user.first()
