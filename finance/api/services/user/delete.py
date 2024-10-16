from django import forms
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.services import Service

from api.models import User


class DeleteUserService(Service):
    id = forms.IntegerField()

    def process(self):
        self.result = self._delete_user
        return self

    @property
    def _delete_user(self):
        obj = self.user_presence()
        obj.delete()
        return True

    def user_presence(self):
        user = User.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise ValidationError(
                message='Пользователь с таким id не существует.',
                response_status=status.HTTP_400_BAD_REQUEST
            )

        return user.first()
