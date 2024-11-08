from service_objects.services import Service
from rest_framework.exceptions import NotFound, ParseError


from api.models import User
from django import forms
from rest_framework import status

class GetUserService(Service):
    id = forms.IntegerField()
    user_id = forms.IntegerField()

    def process(self):
        self.result = self._search_user
        return self

    @property
    def _search_user(self):
        if self.cleaned_data['id'] != self.cleaned_data['user_id']:
            raise ParseError(
                detail='Вы не можете посмотреть данные этого пользователя',
            )
        user = User.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise NotFound(
                detail='Пользователя с таким id не существует.',
            )
        return user.first()

