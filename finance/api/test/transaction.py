import unittest

from api.factories.transaction import TransactionFactory
from api.factories.user import UserFactory
from conf.settings import REST_FRAMEWORK
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestTransaction(APITestCase):
    def setUp(self):
        self.transactions = TransactionFactory.create_batch(3)

        self.user_transaction = UserFactory.create_batch(1)[0]
        Token.objects.create(user=self.user_transaction)
        self.transaction1 = TransactionFactory(user=self.user_transaction)

        self.user1 = UserFactory.create_batch(1)[0]
        self.user2 = UserFactory.create_batch(1)[0]
        Token.objects.create(user=self.user1)
        Token.objects.create(user=self.user2)

    def test_transaction_factory_creates_transactions(self):
        # Проверяем что атрибуты  были созданы
        for transaction in self.transactions:
            self.assertIsNotNone(transaction.user)
            self.assertIsNotNone(transaction.amount)
            self.assertIsNotNone(transaction.date)
            self.assertIsNotNone(transaction.type)
            self.assertIsNotNone(transaction.category)

    def test_transaction_factory_creates_unique_transaction(self):
        transaction1, transaction2 = self.transactions[0], self.transactions[1]

        # Проверяем, что созданные транзакции имеют разные параметры
        self.assertNotEqual(transaction1.user, transaction2.user)
        self.assertNotEqual(transaction1.amount, transaction2.amount)
        self.assertNotEqual(transaction1.category, transaction2.category)
        self.assertNotEqual(transaction1.date, transaction2.date)

    def test_status_authorization_and_len_response(self):
        # Проверяем, что ответ получает только авторизованный пользователь, сравниваем статусы
        # и колличество объектов в ответе (в данном случае ответ равен пагинации указанной в
        # переданном параметре page_size)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user1.auth_token.key)
        response = self.client.get(reverse("create_list_transactions"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), REST_FRAMEWORK["PAGE_SIZE"])

        response2 = self.client.get(reverse("create_list_transactions"), {"page_size": 3})
        self.assertEqual(len(response2.data), 3)

    def test_transaction_creation(self):
        # Тестируем создание новой транзакции
        response = self.client.post(
            reverse("create_list_transactions"),
            {
                "user": self.user1.id,
                "amount": 111.11,
                "type": "доход",
                "category": "new_category",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_access(self):
        # Тестируем доступ без аутентификации
        response = self.client.get(reverse("create_list_transactions"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_transaction_by_id(self):
        # Тестируем получение транзакции по id
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_transaction.auth_token.key)
        response = self.client.get(reverse("get_put_delete_transaction_id", args=[self.transaction1.id]))
        self.assertEqual(self.transaction1.id, response.data["id"])
        self.assertEqual(self.transaction1.amount, float(response.data["amount"]))
        self.assertEqual(self.transaction1.type, response.data["type"])
        self.assertEqual(self.transaction1.category, response.data["category"])
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_put_transaction_by_id(self):
        # Тестируем изменения в атрибутах транзакции
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_transaction.auth_token.key)
        response = self.client.put(
            reverse("get_put_delete_transaction_id", args=[self.transaction1.id]),
            {
                "amount": 999.99,
                "category": "new_put_category",
            },
        )

        self.assertNotEqual(float(response.data["amount"]), self.transaction1.amount)
        self.assertEqual(float(response.data["amount"]), 999.99)

        self.assertNotEqual(response.data["category"], self.transaction1.category)
        self.assertEqual(response.data["category"], "new_put_category")

    def test_delete_transaction_by_id(self):
        # Тестируем удаление транзакции
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_transaction.auth_token.key)
        response = self.client.delete(reverse("get_put_delete_transaction_id", args=[self.transaction1.id]))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)


if __name__ == "__main__":
    unittest.main()
