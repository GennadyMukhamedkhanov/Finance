from api.models import User
from service_objects.services import Service


class ListUsersService(Service):
    def process(self):
        self.result = self._users
        return self

    @property
    def _users(self):
        return User.objects.all().order_by("username")
