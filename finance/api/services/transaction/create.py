from django import forms
from service_objects.services import Service

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
            amount=self.cleaned_data['amount'],
            type=self.cleaned_data['type'],
            category=self.cleaned_data['category']
        )
