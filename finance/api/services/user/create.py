from django import forms
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ParseError
from service_objects.services import Service

from api.models import User


class CreateUsersService(Service):
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField()
    password = forms.CharField()

    def process(self):
        self.user_presence()
        self.result = self._create_user
        return self

    def user_presence(self):
        users = User.objects.filter(email=self.cleaned_data['email'])
        if users.exists():
            raise ParseError(
                detail='Пользователь с таким email уже существует.',
            )

    @property
    def _create_user(self):
        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        self.create_token(user)

        return User

    def create_token(self, user):
        Token.objects.create(user=user)
