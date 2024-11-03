from drf_yasg import openapi
from rest_framework import status

USER_SCHEMA = dict(
    type=openapi.TYPE_OBJECT,
    properties=dict(
        id=openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
        username=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
        email=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
        first_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
        last_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
        password=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

    )
)

TRANSACTION_ITEM = {
    "transaction": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=dict(
            user=openapi.Schema(**USER_SCHEMA),
            amount=openapi.Schema(type=openapi.FORMAT_FLOAT, example="float"),
            date=openapi.Schema(type=openapi.FORMAT_DATETIME, example="string"),
            type=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            category=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

        ),
    ),
}

TRANSACTION_LIST_VIEW = {
    'manual_parameters': [
        openapi.Parameter(
            name='page_size',
            in_=openapi.IN_QUERY,
            description="Переданный параметр page_size "
                        "указывает какое колличество объектов "
                        "транзакций показывать  (query_params)",
            required=False,
            type=openapi.TYPE_NUMBER, ),

    ],
    "operation_id": "Список транзакций",
    "operation_description": """
        Список всех транзакций  на сайте
        page_size по умолчанию равно - 2
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    transaction=openapi.Schema(

                        type=openapi.TYPE_ARRAY,
                        items=TRANSACTION_ITEM["transaction"],
                    ),

                ),

            ),

        ),

    },
}

TRANSACTION_CREATE_VIEW = {
    "operation_id": "Создание транзакции",
    "operation_description": """
        Создание пользователем транзакции
    """,
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "user": openapi.Schema(type=openapi.TYPE_INTEGER, description='ID пользователя'),
            "amount": openapi.Schema(type=openapi.TYPE_STRING, description='Сумма'),
            "type": openapi.Schema(type=openapi.TYPE_STRING, description='Тип (доход/расход)'),
            "category": openapi.Schema(type=openapi.TYPE_STRING, description='Категория'),
        },
        required=["user", "amount", "type", "category"]
    ),
    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "CREATED",

        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            "BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Сумма транзакции должна быть больше нуля",
                }
            },
        )
    },
}

TRANSACTION_GET_VIEW = {

    "operation_id": "Получение транзакции",
    "operation_description": """
        Выводит конкретную транзакцию по переданному id
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    user=openapi.Schema(**USER_SCHEMA),
                    amount=openapi.Schema(type=openapi.FORMAT_FLOAT, example="float"),
                    date=openapi.Schema(type=openapi.FORMAT_DATETIME, example="string"),
                    type=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    category=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

                ),
            ),

        ),

        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Вы не можете посмотреть данные этой транзакции",
                }
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="NOT_FOUND",
            examples={
                "application/json": {
                    "ValidationError": "Транзакции с таким id не существует.",
                }
            },
        )

    },
}



TRANSACTION_PUT_VIEW = {
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "amount": openapi.Schema(type=openapi.TYPE_STRING, description='Сумма'),
            "type": openapi.Schema(type=openapi.TYPE_STRING, description='Тип (доход/расход)'),
            "category": openapi.Schema(type=openapi.TYPE_STRING, description='Категория'),
        },
        required=[]
    ),

    "operation_id": "Изменение данных транзакции",
    "operation_description": """
        Изменяет данные транзакции определенного 
        пользователя по переданному id транзакции
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    user=openapi.Schema(**USER_SCHEMA),
                    amount=openapi.Schema(type=openapi.FORMAT_FLOAT, example="float"),
                    date=openapi.Schema(type=openapi.FORMAT_DATETIME, example="string"),
                    type=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    category=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

                ),
            ),

        ),

        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Вы не можете изменить данные этой транзакции",
                }
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="NOT_FOUND",
            examples={
                "application/json": {
                    "ValidationError": "Транзакции с таким id не существует.",
                }
            },
        )

    },
}



TRANSACTION_DELETE_VIEW = {

    "operation_id": "Удаление транзакции",
    "operation_description": """
        Удаляет конкретную транцакцию по переданному id
    """,
    "responses": {
        status.HTTP_204_NO_CONTENT: openapi.Response(
            description="OK",
        ),

        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Транзакции с таким id не существует.",
                }
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="NOT_FOUND",
            examples={
                "application/json": {
                    "ValidationError": "Вы не можете удалить данные этой транзакции.",
                }
            },
        )

    },
}
