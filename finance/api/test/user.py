import unittest

from api.factories.user import UserFactory
from conf.settings import REST_FRAMEWORK
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestUser(APITestCase):
    def setUp(self):
        self.users = UserFactory.create_batch(3)
        self.user = UserFactory.create_batch(1)[0]
        self.user_del = UserFactory.create_batch(1)[0]
        Token.objects.create(user=self.user)
        Token.objects.create(user=self.user_del)

    def test_user_factory_creates_users(self):
        # Проверяем что атрибуты  были созданы
        for user in self.users:
            self.assertIsNotNone(user.username)
            self.assertIsNotNone(user.email)
            self.assertIsNotNone(user.first_name)
            self.assertIsNotNone(user.last_name)
            self.assertTrue(user.check_password("defaultpassword"))

    def test_user_factory_creates_unique_users(self):
        user1, user2 = self.users[0], self.users[1]

        # Проверяем, что созданные пользователи имеют разные параметры
        self.assertNotEqual(user1.email, user2.email)
        self.assertNotEqual(user1.first_name, user2.first_name)
        self.assertNotEqual(user1.last_name, user2.last_name)
        self.assertNotEqual(user1.username, user2.username)

    def test_user_factory_creates_valid_email(self):
        user = self.users[2]

        # Проверяем, что email имеет правильный формат
        self.assertIn("@", user.email)
        self.assertIn(".", user.email.split("@")[-1])

    def test_status_authorization_and_len_response(self):
        # Проверяем, что ответ получает только авторизованный пользователь, сравниваем статусы
        # и колличество объектов в ответе (в данном случае ответ равен пагинации указанной в настройках)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user.auth_token.key)
        response = self.client.get(reverse("create_list_users"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), REST_FRAMEWORK["PAGE_SIZE"])

        response2 = self.client.get(reverse("create_list_users"), {"page_size": 3})
        self.assertEqual(len(response2.data), 3)

    def test_user_creation(self):
        # Тестируем создание нового пользователя
        response = self.client.post(
            reverse("create_list_users"),
            {
                "username": "new_username",
                "password": "new_password",
                "email": "test@mail.ru",
                "last_name": "last_name",
                "first_name": "first_name",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthorized_access(self):
        # Тестируем доступ без аутентификации
        response = self.client.get(reverse("create_list_users"))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_user_by_id(self):
        # Тестируем получение пользователя по id
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user.auth_token.key)
        response = self.client.get(reverse("get_put_delete_user_id", args=[self.user.id]))
        self.assertEqual(self.user.id, response.data["id"])
        self.assertEqual(self.user.email, response.data["email"])
        self.assertEqual(self.user.first_name, response.data["first_name"])
        self.assertEqual(self.user.last_name, response.data["last_name"])
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_put_user_by_id(self):
        # Тестируем изменения в атрибутах объекта
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user.auth_token.key)
        response = self.client.put(
            reverse("get_put_delete_user_id", args=[self.user.id]),
            {
                "email": "new_put_email@mail.ru",
                "first_name": "new_put_first_name",
                "last_name": "new_put_last_name",
            },
        )

        self.assertNotEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["email"], "new_put_email@mail.ru")

        self.assertNotEqual(response.data["first_name"], self.user.first_name)
        self.assertEqual(response.data["first_name"], "new_put_first_name")

        self.assertNotEqual(response.data["last_name"], self.user.last_name)
        self.assertEqual(response.data["last_name"], "new_put_last_name")

    def test_delete_user_by_id(self):
        # Тестируем удаление объекта
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.user_del.auth_token.key)
        response = self.client.delete(reverse("get_put_delete_user_id", args=[self.user_del.id]))
        self.assertEqual(status.HTTP_204_NO_CONTENT, response.status_code)

        response = self.client.delete(reverse("get_put_delete_user_id", args=[self.user_del.id]))
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)


if __name__ == "__main__":
    unittest.main()
