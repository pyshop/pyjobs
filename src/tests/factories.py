import factory
from adverts.models import Advert
from accounts.models import User
from .utils import random_words
import factory.fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Iterator(random_words(100))
    email = factory.LazyAttribute(lambda o: '%s@example.com' % o.username)
    is_worker = factory.Iterator([False, True, False, True])
    is_recruiter = factory.Iterator([True, False, False, True])


class AdvertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advert

    title = factory.Iterator(random_words(100))
    description = random_words(100)
    requirements = random_words(20)
    salary = factory.fuzzy.FuzzyInteger(10000, 100000)
    city = factory.Iterator(random_words(100))
    is_remote = factory.Iterator([False, True, False, True])
    # author = factory.SubFactory(UserFactory) # будет создавать нового пользователя с объявлением
    author = factory.Iterator(User.objects.all())  # привязывает объявления к существующим пользователям
