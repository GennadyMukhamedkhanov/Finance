import csv

from api.docs.export_transaction import EXPORT_TRANSACTION_VIEW
from api.models import Transaction
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class ExportTransactionsCSV(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    @swagger_auto_schema(**EXPORT_TRANSACTION_VIEW)
    def get(self, request, *args, **kwargs):
        # Создаем HTTP ответ с заголовком для CSV
        response = HttpResponse(content_type="text/csv; charset=utf-8")
        response["Content-Disposition"] = 'attachment; filename="transactions.csv"'

        # Создаем CSV writer
        writer = csv.writer(response)

        # Добавляем пустую строку перед заголовками
        writer.writerow([])  # Пустая строка
        writer.writerow(["Пользователь", "Сумма", "Дата", "Тип", "Категория"])

        # Получаем транзакции для текущего пользователя
        transactions = Transaction.objects.filter(user_id=request.user.id)

        for transaction in transactions:
            writer.writerow(
                [
                    transaction.user.username,
                    transaction.amount,
                    transaction.date.strftime("%Y-%m-%d %H:%M:%S"),
                    transaction.get_type_display(),
                    transaction.category,
                ]
            )

        return response
