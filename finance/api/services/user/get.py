from service_objects.services import Service
from service_objects.errors import ValidationError
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
            raise ValidationError(
                message='Вы не можете посмотреть данные этого пользователя',
                response_status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise ValidationError(
                message='Пользователя с таким id не существует.',
                response_status=status.HTTP_404_NOT_FOUND
            )
        return user.first()

