# Система управления финансами

Это проект по разработке системы управления финансами с расширенными функциями для обработки транзакций. Система
позволяет пользователям отслеживать свои доходы и расходы, управлять бюджетами и генерировать финансовые отчеты.

## Цель

Разработать систему управления финансами с возможностью обработки транзакций, отслеживания бюджета и генерации отчетов.

## Требования

### Среда разработки

- Python 3.8+
- Django 3.2+
- Django REST Framework 3.12+
- PostgreSQL в качестве базы данных

## Установка

Следуйте инструкциям ниже для установки и запуска проекта:

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/GennadyMukhamedkhanov/Finance.git
   ```

2. Перейдите в директорию проекта:
    ```bash
    cd finance
   ```

3. Создайте виртуальное окружение и активируйте его:
    ```bash
   pip install pipenv
   
   
   pipenv shell
   ```

4. Установите зависимости:
    ```bash
   pipenv install
   ```

5. Настройте базу данных PostgreSQL и обновите настройки в settings.py.


6. Примените миграции:
    ```bash
    python manage.py migrate
      ```

7. Создайте суперпользователя:
    ```bash
   python manage.py createsuperuser
      ```

8. Запустите сервер:
    ```bash
   python manage.py runserver    
   ```

# Использование

## API эндпоинты

### Пользователи

- GET /api/users/: Получить список всех пользователей.
- POST /api/user/: Создать нового пользователя.
- GET /api/user/{id}/: Получить информацию о конкретном пользователе по ID.
- PUT /api/user/{id}/: Обновить информацию о конкретном пользователе по ID.
- DELETE /api/user/{id}/: Удалить конкретного пользователя по ID.

### Транзакции

- GET /api/transactions/: Получить список всех транзакций.
- POST /api/transactions/: Создать новую транзакцию.
- GET /api/transaction/{id}/: Получить информацию о конкретной транзакции по ID.
- PUT /api/transaction/{id}/: Обновить информацию о конкретной транзакции по ID.
- DELETE /api/transaction/{id}/: Удалить конкретную транзакцию по ID.

### Экспорт данных

- GET /api/export/transactions/csv/ Экспорт данных транзакции и отчетов в формате CSV

# Валидация

- Проверка валидности email пользователя.
- Проверка, что сумма транзакции является положительным числом.

# Тестирование

- Написаны unit-тесты для моделей.
- Написаны интеграционные тесты для API эндпоинтов.

### Запустить тесты

   ```bash
   python manage.py test
```

# Контакты 
## Буду рад пообщаться и обсудить возможности нашего дальнейшего сотрудничества.
### Я всегда на связи:
- телефон: 8-977-294-12-18
- телеграм: https://t.me/Gennadius777
- email: dungreshmen2@mail.ru