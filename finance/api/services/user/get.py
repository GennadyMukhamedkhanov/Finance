from service_objects.services import Service
from service_objects.errors import ValidationError
from api.models import User
from django import forms
from rest_framework import status

class GetUserService(Service):
    id = forms.IntegerField()

    def process(self):
        self.result = self._search_user
        return self

    @property
    def _search_user(self):
        user = User.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise ValidationError(
                message='Пользователь с таким id не существует.',
                response_status=status.HTTP_404_NOT_FOUND
            )
        return user.first()

