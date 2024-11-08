from django import forms
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError

from service_objects.services import Service

from api.models import Transaction, User


class PutTransactionService(Service):
    id = forms.IntegerField()
    user_id = forms.IntegerField()
    user = forms.IntegerField(required=False)
    amount = forms.DecimalField(required=False)
    date = forms.DateTimeField(required=False)
    type = forms.CharField(required=False)
    category = forms.CharField(required=False)

    def process(self):
        self.check_positive_number(self.cleaned_data['amount'])
        self.result = self._update_transaction
        return self

    @property
    def _update_transaction(self):
        obj = self.transaction_presence()
        obj.user.id = self.cleaned_data['user'] if self.user_presence() else obj.user
        obj.amount = self.cleaned_data['amount'] if self.cleaned_data['amount'] else obj.amount
        obj.date = self.cleaned_data['date'] if self.cleaned_data['date'] else obj.date
        obj.type = self.cleaned_data['type'] if self.cleaned_data['type'] else obj.type
        obj.category = self.cleaned_data['category'] if self.cleaned_data['category'] else obj.category
        obj.save()
        return obj

    def transaction_presence(self):
        transaction = Transaction.objects.filter(id=self.cleaned_data['id'])
        if not transaction.exists():
            raise NotFound(
                detail='Транзакции с таким id не существует.',
            )
        if transaction.first().user.id != self.cleaned_data['user_id']:
            raise ParseError(
                detail='Вы не можете изменить данные этой транзакции',
            )

        return transaction.first()

    def user_presence(self):
        if self.cleaned_data['user']:
            user = User.objects.filter(id=self.cleaned_data['user'])
            if not user.exists():
                raise ValidationError(
                    message='Пользователя с  переданным id не существует.',
                    response_status=status.HTTP_400_BAD_REQUEST
                )
            return True
        return False

    @staticmethod
    def check_positive_number(num):
        if num <= 0:
            raise ValidationError(
                message='Сумма транзакции должна быть больше нуля',
                response_status=status.HTTP_400_BAD_REQUEST
            )
