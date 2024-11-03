from drf_yasg import openapi
from rest_framework import status

EXPORT_TRANSACTION_VIEW = {

    "operation_id": "Экспорта данных транзакций",
    "operation_description": """
        Экспорта данных транзакций и составление отчета в формате CSV
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",

        ),

    }
}
