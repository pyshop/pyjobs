from django.core.management.base import BaseCommand
from tests.factories import UserFactory


class Command(BaseCommand):
    help = 'creates sample data from factory'

    def handle(self, *args, **options):
        return UserFactory.create_batch(size=15)
