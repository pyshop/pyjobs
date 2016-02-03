import factory
from adverts.models import Advert


class AdvertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advert

    title = factory.Sequence(lambda n: 'Программист%s' % n)
    description = factory.Sequence(lambda n: 'требуется самый лучший программист%s' % n)
    requirements = factory.Sequence(lambda n: 'ничего не требуется%s' % n)
    salary = factory.Sequence(lambda n: '234%s' % n)
    city = factory.Sequence(lambda n: 'москва%s' % n)
    is_remote = factory.Iterator("True", "False")
