from django import forms
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError


from service_objects.services import Service

from api.models import User


class DeleteUserService(Service):
    id = forms.IntegerField()
    user_id = forms.IntegerField()

    def process(self):
        self.result = self._delete_user
        return self

    @property
    def _delete_user(self):
        obj = self.user_presence()
        obj.delete()
        return True

    def user_presence(self):
        if self.cleaned_data['id'] != self.cleaned_data['user_id']:
            raise ParseError(
                detail='Вы не можете удалить данные этого пользователя',
            )
        user = User.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise NotFound(
                detail='Пользователь с таким id не существует.',
            )

        return user.first()
