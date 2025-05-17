from api.models import Transaction
from django import forms
from rest_framework.exceptions import NotFound, ParseError
from service_objects.services import Service


class GetTransactionService(Service):
    id = forms.IntegerField()
    user_id = forms.IntegerField()

    def process(self):
        self.result = self._search_transaction
        return self

    @property
    def _search_transaction(self):
        transaction = Transaction.objects.filter(id=self.cleaned_data["id"])
        if not transaction.exists():
            raise NotFound(
                detail="Транзакции с таким id не существует.",
            )
        if transaction.first().user.id != self.cleaned_data["user_id"]:
            raise ParseError(
                detail="Вы не можете удалить данные этой транзакции",
            )
        return transaction.first()
