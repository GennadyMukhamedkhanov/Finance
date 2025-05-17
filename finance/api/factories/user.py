import factory
from api.models import User
from faker import Faker

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: fake.user_name())
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    password = factory.PostGenerationMethodCall("set_password", "defaultpassword")
