import csv
from django.http import HttpResponse
from rest_framework.views import APIView

from api.models import Transaction, User


class ExportTransactionsCSV(APIView):
    def get(self, request, *args, **kwargs):
        # Создаем HTTP ответ с заголовком для CSV
        response = HttpResponse(content_type='text/csv; charset=utf-8')
        response['Content-Disposition'] = 'attachment; filename="transactions.csv"'

        # Создаем CSV writer
        writer = csv.writer(response)

        # Добавляем пустую строку перед заголовками
        writer.writerow([])  # Пустая строка
        writer.writerow(['Пользователь', 'Сумма', 'Дата', 'Тип', 'Категория'])

        user = User.objects.get(id=1204)

        # Получаем транзакции для текущего пользователя
        transactions = Transaction.objects.filter(user=user)

        for transaction in transactions:
            writer.writerow([

                transaction.user.username,
                transaction.amount,
                transaction.date.strftime('%Y-%m-%d %H:%M:%S'),
                transaction.get_type_display(),
                transaction.category,
            ])

        return response