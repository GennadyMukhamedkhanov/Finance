from service_objects.services import Service
from api.models import Transaction


class ListTransactionsService(Service):

    def process(self):
        self.result = self._transactions
        return self

    @property
    def _transactions(self):
        return Transaction.objects.all()
