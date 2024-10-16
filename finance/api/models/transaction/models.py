from django.db import models


class Transaction(models.Model):
    INCOME = 'доход'
    EXPENSE = 'расход'
    TRANSACTION_TYPES = [
        (INCOME, 'Доход'),
        (EXPENSE, 'Расход'),
    ]

    user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='Пользователь', related_name='transactions')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма')
    date = models.DateTimeField(verbose_name='Дата', auto_now_add=True)
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES, verbose_name='Тип')
    category = models.CharField(max_length=50, verbose_name='Категория')

    class Meta:
        db_table = 'transaction'
        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f"{self.type} - {self.amount}"
