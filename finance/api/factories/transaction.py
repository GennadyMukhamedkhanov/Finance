import factory
from api.factories.user import UserFactory
from api.models import Transaction
from faker import Faker

fake = Faker()


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    user = factory.SubFactory(UserFactory)
    amount = factory.LazyFunction(lambda: round(fake.random.uniform(1, 1000), 2))
    type = factory.Iterator([Transaction.INCOME, Transaction.EXPENSE])
    category = factory.LazyAttribute(lambda _: fake.word())
    date = factory.LazyFunction(fake.date_time)
