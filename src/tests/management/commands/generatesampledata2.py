from django.core.management.base import BaseCommand
from tests.factories import AdvertFactory


class Command(BaseCommand):
    help = 'creates sample data from factory'

    def handle(self, *args, **options):
        return AdvertFactory.create_batch(size=10)
