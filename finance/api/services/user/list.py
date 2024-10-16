from service_objects.services import Service
from api.models import User


class ListUsersService(Service):

    def process(self):
        self.result = self._users
        return self

    @property
    def _users(self):
        return User.objects.all()
