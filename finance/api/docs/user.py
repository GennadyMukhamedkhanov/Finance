from drf_yasg import openapi
from rest_framework import status

USER_ITEM = {
    "users": openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties=dict(
            id=openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
            username=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            email=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            first_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            last_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
            password=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

        ),
    ),
}

USER_CREATE_VIEW = {
    "operation_id": "Регистрация пользователя",
    "operation_description": """
        Регистрация пользователя на сайте
    """,
    'manual_parameters': [
        openapi.Parameter('email', openapi.IN_QUERY,
                          description="Почта пользователя (body)",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('first_name', openapi.IN_QUERY,
                          description="Имя пользователя (body)",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('last_name', openapi.IN_QUERY,
                          description="Фамилия пользователя (body)",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('username', openapi.IN_QUERY,
                          description="Логин пользователя (body)",
                          type=openapi.TYPE_STRING,
                          required=True),
        openapi.Parameter('password', openapi.IN_QUERY,
                          description="Пароль пользователя (body)",
                          type=openapi.TYPE_STRING,
                          required=True),

    ],
    "responses": {
        status.HTTP_201_CREATED: openapi.Response(
            "CREATED",

        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            "BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Пользователь с таким email уже существует.",
                }
            },
        )
    },
}

USER_LIST_VIEW = {

    'manual_parameters': [
        openapi.Parameter(
            name='page_size',
            in_=openapi.IN_QUERY,
            description="Переданный параметр page_size "
                        "указывает какое колличество объектов "
                        "user показывать  (query_params)",
            required=False,
            type=openapi.TYPE_NUMBER, ),

    ],
    "operation_id": "Список пользователей",
    "operation_description": """
        Список всех пользователей зарегистрированных на сайте
        page_size по умолчанию равно - 2
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    users=openapi.Schema(
                        type=openapi.TYPE_ARRAY,
                        items=USER_ITEM["users"],
                    ),

                ),

            ),

        ),

    },
}

USER_GET_VIEW = {

    "operation_id": "Получение пользователя",
    "operation_description": """
        Выводит конкретного пользователя по переданному id
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    id=openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    username=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    email=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    first_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    last_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    password=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

                ),

            ),

        ),

        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Вы не можете посмотреть данные этого пользователя.",
                }
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="NOT_FOUND",
            examples={
                "application/json": {
                    "ValidationError": "Пользователя с таким id не существует.",
                }
            },
        )

    },
}

USER_PUT_VIEW = {
    'request_body': openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Новый логин пользователя'),
            'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Новое имя пользователя'),
            'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Новая фамилия пользователя'),
            'email': openapi.Schema(type=openapi.FORMAT_EMAIL, description='Новая почта пользователя'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, description='Новый пароль пользователя'),
        },
        required=[]
    ),

    "operation_id": "Изменение данных пользователя",
    "operation_description": """
        Изменяет данные конкретного пользователя по переданному id
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties=dict(
                    id=openapi.Schema(type=openapi.TYPE_INTEGER, example=1),
                    username=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    email=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    first_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    last_name=openapi.Schema(type=openapi.TYPE_STRING, example="string"),
                    password=openapi.Schema(type=openapi.TYPE_STRING, example="string"),

                ),

            ),

        ),

        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Вы не можете изменить данные этого пользователя",
                }
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="NOT_FOUND",
            examples={
                "application/json": {
                    "ValidationError": "Пользователя с таким id не существует.",
                }
            },
        )

    },
}

USER_DELETE_VIEW = {

    "operation_id": "Удаление пользователя",
    "operation_description": """
        Удаляет конкретного пользователя по переданному id
    """,
    "responses": {
        status.HTTP_200_OK: openapi.Response(
            description="OK",
        ),

        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description="BAD_REQUEST",
            examples={
                "application/json": {
                    "ValidationError": "Вы не можете удалить данные этого пользователя",
                }
            },
        ),
        status.HTTP_404_NOT_FOUND: openapi.Response(
            description="NOT_FOUND",
            examples={
                "application/json": {
                    "ValidationError": "Пользователь с таким id не существует.",
                }
            },
        )

    },
}
