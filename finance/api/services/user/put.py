from django import forms
from rest_framework import status
from service_objects.errors import ValidationError
from service_objects.services import Service

from api.models import User


class PutUserService(Service):
    id = forms.IntegerField()
    user_id = forms.IntegerField()
    email = forms.EmailField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)

    def process(self):
        self.result = self._update_user
        return self

    @property
    def _update_user(self):
        obj = self.user_presence()
        obj.email = self.cleaned_data['email'] if self.email_presence(obj) else obj.email
        obj.first_name = self.cleaned_data['first_name'] if self.cleaned_data['first_name'] else obj.first_name
        obj.last_name = self.cleaned_data['last_name'] if self.cleaned_data['last_name'] else obj.last_name
        obj.username = self.cleaned_data['username'] if self.cleaned_data['username'] else obj.username
        obj.password = self.cleaned_data['password'] if self.cleaned_data['password'] else obj.password
        obj.save()
        return obj

    def user_presence(self):
        if self.cleaned_data['id'] != self.cleaned_data['user_id']:
            raise ValidationError(
                message='Вы не можете изменить данные этого пользователя',
                response_status=status.HTTP_400_BAD_REQUEST
            )
        user = User.objects.filter(id=self.cleaned_data['id'])
        if not user.exists():
            raise ValidationError(
                message='Пользователь с таким id не существует.',
                response_status=status.HTTP_400_BAD_REQUEST
            )

        return user.first()

    def email_presence(self, obj):
        email = self.cleaned_data.get('email')
        if email:
            user = User.objects.filter(email=email).first()
            if user and user != obj:
                raise ValidationError(
                    'Пользователь с таким email уже существует.',
                    response_status=status.HTTP_400_BAD_REQUEST
                )
            return True
        return False
