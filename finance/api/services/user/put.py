from api.models import User
from django import forms
from rest_framework.exceptions import ParseError
from service_objects.services import Service


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
        obj.email = self.cleaned_data["email"] if self.email_presence(obj) else obj.email
        obj.first_name = self.cleaned_data["first_name"] if self.cleaned_data["first_name"] else obj.first_name
        obj.last_name = self.cleaned_data["last_name"] if self.cleaned_data["last_name"] else obj.last_name
        obj.username = self.cleaned_data["username"] if self.cleaned_data["username"] else obj.username
        obj.password = self.cleaned_data["password"] if self.cleaned_data["password"] else obj.password
        obj.save()
        return obj

    def user_presence(self):
        if self.cleaned_data["id"] != self.cleaned_data["user_id"]:
            raise ParseError(
                detail="Вы не можете изменить данные этого пользователя",
            )
        user = User.objects.filter(id=self.cleaned_data["id"])
        if not user.exists():
            raise ParseError(
                detail="Пользователь с таким id не существует.",
            )

        return user.first()

    def email_presence(self, obj):
        email = self.cleaned_data.get("email")
        if email:
            user = User.objects.filter(email=email).first()
            if user and user != obj:
                raise ParseError(
                    detail="Пользователь с таким email уже существует.",
                )
            return True
        return False
