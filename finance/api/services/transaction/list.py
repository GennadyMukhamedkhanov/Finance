from api.models import Transaction
from service_objects.services import Service


class ListTransactionsService(Service):
    def process(self):
        self.result = self._transactions
        return self

    @property
    def _transactions(self):
        return Transaction.objects.all().order_by("id")
